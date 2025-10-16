\ifndef{threeSecurityExamplesOpening}
\define{threeSecurityExamplesOpening}

\editme

\subsection{Three Security Examples}

\notes{Let me start with three practical examples that illustrate the evolution of security challenges we're facing today.}

\subsection{1. Safety on Airplanes}
\slides{
\aligncenter{What Cursor wrote for me at 39,000 ft}
```
rm -rf ~/
```
}

\notes{}

\subsection{2. Security at the Gate}
\slides{
* Heathrow/Brussels airport cyber-attack
* Collins Aerospace systems compromised  
* Traditional infrastructure vulnerabilities
* Single point of failure in critical systems
}

\notes{In September 2025, a cyber-attack on Collins Aerospace systems caused massive disruption across European airports including Heathrow, Brussels, and Berlin. The attack targeted the Muse software system that allows different airlines to share check-in desks and boarding gates.

This is a classic example of traditional infrastructure vulnerabilities:
- Single point of failure in critical systems
- Cascading effects across multiple airports  
- Manual fallback procedures (pen and paper check-in)
- Hours-long delays and flight cancellations

The attack demonstrates how our critical infrastructure remains vulnerable to classical cyber-attacks, even in 2025.}

\subsection{3. Agent Safety}
\slides{
* Notion AI Agents security research
* Indirect prompt injection attacks
* HAM vulnerabilities exposed
* "Lethal trifecta" of LLM agents, tool access, and long-term memory
}

\notes{The CodeIntegrity research highlights the new class of security vulnerabilities. Indirect prompt injection attacks can be used to exfiltrate sensitive data, e.g. from private Notion workspaces.

The attack works by:
- Embedding malicious prompts in seemingly innocent documents
- Tricking AI agents into performing unauthorized actions
- Using the *lethal trifecta* of LLM agents, tool access, and long-term memory
- Bypassing traditional RBAC (Role-Based Access Control) systems

This represents a fundamental shift in attack vectors - we're no longer just dealing with traditional infrastructure vulnerabilities, but with AI systems that can be manipulated through natural language.}


\endif
