#!/usr/bin/env python3
"""
Find references to snippet files that need to be renamed.

Searches in specified directories (like talks/ and mlatcl/*/_lamd/) for
references to the old filenames and reports where they need to be updated.
"""

import sys
import re
from pathlib import Path
from typing import List, Tuple, Dict


def load_filename_changes(changes_file: Path) -> List[Tuple[str, str]]:
    """Load the filename changes mapping.
    
    Returns:
        List of (old_filename, new_filename) tuples (just the basenames)
    """
    changes = []
    with open(changes_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('#') or '->' not in line:
                continue
            
            old_path, new_path = line.split(' -> ')
            old_name = Path(old_path).name
            new_name = Path(new_path).name
            
            # Skip if they're the same (e.g., the .# file)
            if old_name != new_name:
                changes.append((old_name, new_name))
    
    return changes


def search_for_references(search_dirs: List[Path], old_filename: str) -> List[Tuple[Path, int, str]]:
    """Search for references to a filename in the given directories.
    
    Returns:
        List of (file_path, line_number, line_content) tuples
    """
    matches = []
    
    # Search for the filename without extension too
    basename_no_ext = old_filename.replace('.md', '')
    
    for search_dir in search_dirs:
        if not search_dir.exists():
            continue
            
        # Search all text files (md, yml, yaml, txt, etc.)
        for ext in ['*.md', '*.yml', '*.yaml', '*.txt', '*.html', '*.ipynb']:
            for file_path in search_dir.rglob(ext):
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        for line_num, line in enumerate(f, 1):
                            # Check if the old filename appears in the line
                            if old_filename in line or basename_no_ext in line:
                                matches.append((file_path, line_num, line.strip()))
                except Exception:
                    # Skip files that can't be read
                    pass
    
    return matches


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Find references to files that need renaming'
    )
    parser.add_argument(
        '--changes-file',
        default='filename_changes.txt',
        help='File containing the old->new filename mappings'
    )
    parser.add_argument(
        '--search-dirs',
        nargs='+',
        help='Directories to search for references (supports glob patterns)'
    )
    parser.add_argument(
        '--summary-only',
        action='store_true',
        help='Only show summary counts, not individual matches'
    )
    
    args = parser.parse_args()
    
    # Load the filename changes
    changes_file = Path(args.changes_file)
    if not changes_file.exists():
        print(f"Error: Changes file not found: {changes_file}")
        return 1
    
    changes = load_filename_changes(changes_file)
    print(f"Loaded {len(changes)} filename changes\n")
    
    # Determine search directories
    if args.search_dirs:
        search_dirs = []
        for pattern in args.search_dirs:
            # Handle glob patterns
            pattern_path = Path(pattern).expanduser()
            if '*' in str(pattern_path):
                # Get parent and glob from there
                parts = str(pattern_path).split('*', 1)
                parent = Path(parts[0]).parent if parts[0] else Path.home()
                search_dirs.extend(parent.glob(str(pattern_path).replace(str(parent) + '/', '')))
            else:
                search_dirs.append(pattern_path)
    else:
        # Default search locations
        search_dirs = []
        
        # 1. Local snippets directory (current directory)
        search_dirs.append(Path('.'))
        
        # 2. ~/lawrennd/talks/_* directories
        talks_parent = Path.home() / 'lawrennd' / 'talks'
        if talks_parent.exists():
            for subdir in talks_parent.glob('_*'):
                if subdir.is_dir():
                    search_dirs.append(subdir)
        
        # 3. ~/mlatcl/*/_lamd directories
        mlatcl_parent = Path.home() / 'mlatcl'
        if mlatcl_parent.exists():
            for subdir in mlatcl_parent.iterdir():
                if subdir.is_dir():
                    lamd_dir = subdir / '_lamd'
                    if lamd_dir.exists():
                        search_dirs.append(lamd_dir)
    
    if not search_dirs:
        print("No search directories found. Specify with --search-dirs")
        return 1
    
    print(f"Searching in {len(search_dirs)} directories:")
    for d in search_dirs:
        print(f"  - {d}")
    print()
    
    # Search for references to each old filename
    total_matches = 0
    files_with_matches = {}  # old_filename -> list of (file, line_num, line)
    
    for old_name, new_name in changes:
        matches = search_for_references(search_dirs, old_name)
        if matches:
            files_with_matches[old_name] = (new_name, matches)
            total_matches += len(matches)
    
    # Report results
    if not files_with_matches:
        print("✅ No references found to any of the files being renamed!")
        return 0
    
    print(f"Found {total_matches} references to {len(files_with_matches)} files:\n")
    print("="*80)
    
    for old_name, (new_name, matches) in sorted(files_with_matches.items()):
        print(f"\n📄 {old_name} -> {new_name}")
        print(f"   {len(matches)} reference(s) found:")
        
        if not args.summary_only:
            for file_path, line_num, line_content in matches:
                # Show relative path
                try:
                    rel_path = file_path.relative_to(Path.cwd())
                except ValueError:
                    rel_path = file_path
                
                print(f"   {rel_path}:{line_num}")
                print(f"      {line_content[:100]}")
        else:
            # Just show which files
            unique_files = set(f for f, _, _ in matches)
            for file_path in sorted(unique_files):
                try:
                    rel_path = file_path.relative_to(Path.cwd())
                except ValueError:
                    rel_path = file_path
                print(f"   {rel_path}")
    
    print("\n" + "="*80)
    print(f"\n📊 Summary: {total_matches} references in {len(files_with_matches)} files need updating")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())

