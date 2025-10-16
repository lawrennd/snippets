\ifndef{genaiSpecificSecurityChallenges}
\define{genaiSpecificSecurityChallenges}

\editme

\subsection{(Gen)AI-Specific Security Challenges}

\newslide{AI Attack Vectors}
\slides{
* Prompt injection attacks
* Model extraction
* Data poisoning
* Adversarial examples
}

\notes{The Notion AI Agents research reveals a new class of security challenges that are unique to generative AI systems. These challenges go beyond traditional security problems and require fundamentally different approaches to security design.

**Prompt Injection Attacks**: The Notion example demonstrates how indirect prompt injection can be used to manipulate AI systems:
- **Embedded instructions**: Malicious prompts hidden in seemingly innocent documents
- **Authority manipulation**: Exploiting the AI's tendency to follow instructions from perceived authorities
- **Context switching**: Using the AI's ability to process multiple contexts simultaneously
- **Persistence**: Malicious instructions that persist across multiple interactions}

\newslide{HAM-Specific Vulnerabilities}
\slides{
* Indirect prompt injection
* Authority manipulation
* Data exfiltration
* RBAC bypass
}

\newslide{The "Lethal Trifecta"}
\slides{
* LLM agents: AI systems that understand natural language
* Tool access: Ability to interact with external systems
* Long-term memory: Persistent state that can be manipulated
* Creates vulnerabilities unique to HAM systems
}

\notes{The Notion research identifies the "lethal trifecta" of vulnerabilities:
- **LLM agents**: AI systems that can understand and respond to natural language
- **Tool access**: Ability to interact with external systems and data
- **Long-term memory**: Persistent state that can be manipulated over time

This combination creates vulnerabilities that are unique to HAM systems and cannot be addressed through traditional security approaches.

**Indirect Prompt Injection**: The Notion research demonstrates how indirect prompt injection can be used to manipulate HAM systems:
- **Document embedding**: Malicious instructions embedded in documents that appear innocent
- **Authority assertion**: Claims of authority that the AI system accepts
- **False urgency**: Creating artificial urgency to bypass normal security checks
- **Technical legitimacy**: Using technical language to make malicious instructions appear legitimate}

\newslide{Trent.AI Solution}
\slides{* Detect problematic prompts early.
}
\notes{}

\endif
