#!/usr/bin/env python3
r"""
Validate that _*/includes/*.md files have correct \ifndef, \define, and \endif structure.

Usage:
    python scripts/validate_includes.py [--fix]
    
Options:
    --fix    Automatically fix files with incorrect structure
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple


def kebab_to_camel(kebab_str: str) -> str:
    """Convert kebab-case to camelCase.
    
    Args:
        kebab_str: String in kebab-case (e.g., 'simple-transformer-implementation')
        
    Returns:
        String in camelCase (e.g., 'simpleTransformerImplementation')
    """
    parts = kebab_str.split('-')
    # First part stays lowercase, rest are capitalized
    return parts[0].lower() + ''.join(word.capitalize() for word in parts[1:])


def is_valid_filename(filename: str) -> bool:
    """Check if filename is in valid kebab-case format.
    
    Args:
        filename: Filename without extension
        
    Returns:
        True if filename is valid kebab-case (lowercase with hyphens only)
    """
    # Should only contain lowercase letters, numbers, and hyphens
    import re
    return bool(re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', filename))


def validate_file(file_path: Path) -> Tuple[bool, List[str]]:
    r"""Validate that a file has correct \ifndef, \define, and \endif structure.
    
    Args:
        file_path: Path to the file to validate
        
    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    errors = []
    
    # Get the filename without extension
    filename_without_ext = file_path.stem  # e.g., 'simple-transformer-implementation'
    
    # First check: filename should be in kebab-case
    if not is_valid_filename(filename_without_ext):
        # Try to suggest the correct filename
        suggested = filename_without_ext.replace('_', '-').lower()
        errors.append(f"⚠️  FILENAME ERROR: File should be renamed to: {suggested}.md")
        errors.append(f"   Current filename uses invalid format (should be kebab-case)")
    
    # Get the expected camelCase name from the filename
    expected_camel = kebab_to_camel(filename_without_ext.replace('_', '-').lower())
    
    # Read the file
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        errors.append(f"Could not read file: {e}")
        return False, errors
    
    if len(lines) == 0:
        errors.append("File is empty")
        return False, errors
    
    # Check first line: \ifndef{camelCase}
    first_line = lines[0].strip()
    expected_ifndef = f"\\ifndef{{{expected_camel}}}"
    if first_line != expected_ifndef:
        errors.append(f"First line should be: {expected_ifndef}")
        errors.append(f"  Found: {first_line}")
    
    # Check second line (if exists): \define{camelCase}
    if len(lines) < 2:
        errors.append("File should have at least 2 lines (\\ifndef and \\define)")
        return False, errors
    
    second_line = lines[1].strip()
    expected_define = f"\\define{{{expected_camel}}}"
    if second_line != expected_define:
        errors.append(f"Second line should be: {expected_define}")
        errors.append(f"  Found: {second_line}")
    
    # Check last non-blank line: \endif
    # Strip trailing blank lines and whitespace
    last_line = ""
    for line in reversed(lines):
        stripped = line.strip()
        if stripped:
            last_line = stripped
            break
    
    expected_endif = "\\endif"
    if last_line != expected_endif:
        errors.append(f"Last non-blank line should be: {expected_endif}")
        errors.append(f"  Found: {last_line}")
    
    # Check for duplicate consecutive \endif at the end
    endif_count = 0
    for line in reversed(lines):
        stripped = line.strip()
        if stripped == expected_endif:
            endif_count += 1
        elif stripped:  # Non-empty, non-endif line
            break
    
    if endif_count > 1:
        errors.append(f"Found {endif_count} consecutive \\endif statements at end of file (should be exactly 1)")
    
    return len(errors) == 0, errors


def fix_file(file_path: Path) -> bool:
    r"""Automatically fix a file's \ifndef, \define, and \endif structure.
    
    Note: This only fixes the file content, not the filename itself.
    
    Args:
        file_path: Path to the file to fix
        
    Returns:
        True if file was fixed successfully, False otherwise
    """
    filename_without_ext = file_path.stem
    # Convert to camelCase (handling potential underscore cases)
    expected_camel = kebab_to_camel(filename_without_ext.replace('_', '-').lower())
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"  ❌ Could not read file: {e}")
        return False
    
    if len(lines) < 3:
        print(f"  ❌ File too short to fix automatically")
        return False
    
    # Fix first line
    lines[0] = f"\\ifndef{{{expected_camel}}}\n"
    
    # Fix second line
    lines[1] = f"\\define{{{expected_camel}}}\n"
    
    # Find and fix last non-blank line
    # Strip trailing blank lines, replace last non-blank line with \endif, ensure file ends with newline
    while lines and lines[-1].strip() == '':
        lines.pop()
    
    # Remove any duplicate consecutive \endif at the end
    while len(lines) > 1 and lines[-1].strip() == "\\endif" and lines[-2].strip() == "\\endif":
        lines.pop()
    
    if lines:
        lines[-1] = "\\endif\n"
    else:
        # Should not happen if file has content, but handle gracefully
        lines = [f"\\ifndef{{{expected_camel}}}\n", f"\\define{{{expected_camel}}}\n", "\\endif\n"]
    
    # Write back
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        return True
    except Exception as e:
        print(f"  ❌ Could not write file: {e}")
        return False


def find_include_files(root_dir: Path = None) -> List[Path]:
    """Find all _*/includes/*.md files.
    
    Args:
        root_dir: Root directory to search (defaults to current directory)
        
    Returns:
        List of Path objects for matching files
    """
    if root_dir is None:
        root_dir = Path.cwd()
    
    # Find all files matching the pattern _*/includes/*.md
    include_files = []
    for pattern_dir in root_dir.glob('_*'):
        if pattern_dir.is_dir():
            includes_dir = pattern_dir / 'includes'
            if includes_dir.exists() and includes_dir.is_dir():
                include_files.extend(includes_dir.glob('*.md'))
    
    return sorted(include_files)


def main():
    """Main entry point for the validation script."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Validate _*/includes/*.md files have correct \\ifndef, \\define, and \\endif'
    )
    parser.add_argument('--fix', action='store_true', help='Automatically fix files')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be fixed without making changes')
    parser.add_argument('files', nargs='*', help='Specific files to check (defaults to all)')
    
    args = parser.parse_args()
    
    # Get files to check
    if args.files:
        files_to_check = [Path(f) for f in args.files]
    else:
        files_to_check = find_include_files()
    
    if not files_to_check:
        print("No files found matching pattern _*/includes/*.md")
        return 0
    
    print(f"Checking {len(files_to_check)} files...\n")
    
    invalid_files = []
    
    for file_path in files_to_check:
        is_valid, errors = validate_file(file_path)
        
        if not is_valid:
            invalid_files.append(file_path)
            # Try to show relative path, fall back to absolute if needed
            try:
                display_path = file_path.relative_to(Path.cwd())
            except ValueError:
                display_path = file_path
            print(f"❌ {display_path}")
            for error in errors:
                print(f"  {error}")
            
            if args.dry_run:
                print(f"  🔍 [DRY RUN] Would attempt to fix ifndef/define/endif lines")
                # Show what would be changed
                filename_without_ext = file_path.stem
                expected_camel = kebab_to_camel(filename_without_ext.replace('_', '-').lower())
                print(f"      Would set to: \\ifndef{{{expected_camel}}} and \\define{{{expected_camel}}}")
            elif args.fix:
                print(f"  🔧 Attempting to fix...")
                if fix_file(file_path):
                    print(f"  ✅ Fixed!")
                    # Re-validate
                    is_valid_after_fix, _ = validate_file(file_path)
                    if is_valid_after_fix:
                        invalid_files.remove(file_path)
            print()
    
    # Summary
    if invalid_files:
        print(f"\n❌ {len(invalid_files)} file(s) with errors")
        if args.dry_run:
            print("\nThis was a dry run. Run with --fix to actually make changes.")
        elif not args.fix:
            print("\nRun with --dry-run to see what would be fixed")
            print("Run with --fix to automatically correct these files")
        return 1
    else:
        print(f"✅ All {len(files_to_check)} files are valid!")
        return 0


if __name__ == '__main__':
    sys.exit(main())

