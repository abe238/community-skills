#!/usr/bin/env python3
"""
Prompt Analyzer Script
Analyzes prompts and recommends optimization techniques based on Anthropic's research.
"""

import re
import json
from typing import Dict, List, Tuple

class PromptAnalyzer:
    def __init__(self):
        self.core_techniques = [
            "be_clear_direct",
            "use_examples", 
            "chain_of_thought",
            "xml_tags",
            "role_prompting",
            "prefill_response",
            "chain_prompts"
        ]
        
    def analyze_prompt(self, prompt: str) -> Dict:
        """Analyze a prompt and return optimization recommendations."""
        analysis = {
            "clarity_score": self._assess_clarity(prompt),
            "structure_score": self._assess_structure(prompt),
            "complexity_level": self._assess_complexity(prompt),
            "missing_techniques": self._identify_missing_techniques(prompt),
            "recommendations": []
        }
        
        # Generate recommendations based on analysis
        analysis["recommendations"] = self._generate_recommendations(analysis, prompt)
        
        return analysis
    
    def _assess_clarity(self, prompt: str) -> int:
        """Assess prompt clarity on scale 1-10."""
        score = 5  # baseline
        
        # Check for context indicators
        context_indicators = ["context", "background", "purpose", "goal", "audience"]
        if any(indicator in prompt.lower() for indicator in context_indicators):
            score += 2
            
        # Check for success criteria
        success_indicators = ["success", "good", "quality", "criteria", "measure"]
        if any(indicator in prompt.lower() for indicator in success_indicators):
            score += 1
            
        # Penalize vague language
        vague_terms = ["something", "anything", "stuff", "things"]
        vague_count = sum(prompt.lower().count(term) for term in vague_terms)
        score -= min(vague_count, 3)
        
        return max(1, min(10, score))
    
    def _assess_structure(self, prompt: str) -> int:
        """Assess prompt structure on scale 1-10."""
        score = 3  # baseline
        
        # Check for XML tags
        if re.search(r'<\w+>', prompt):
            score += 3
            
        # Check for examples
        if 'example' in prompt.lower() or re.search(r'input.*output', prompt, re.IGNORECASE):
            score += 2
            
        # Check for step-by-step structure
        if re.search(r'\d+\.|\bstep\b', prompt, re.IGNORECASE):
            score += 2
            
        return max(1, min(10, score))
    
    def _assess_complexity(self, prompt: str) -> str:
        """Assess task complexity: simple, medium, complex."""
        complexity_indicators = {
            'simple': ['list', 'define', 'what is', 'explain'],
            'medium': ['analyze', 'compare', 'evaluate', 'summarize'],
            'complex': ['synthesize', 'design', 'create', 'optimize', 'multi-step']
        }
        
        prompt_lower = prompt.lower()
        
        for level, indicators in complexity_indicators.items():
            if any(indicator in prompt_lower for indicator in indicators):
                if level == 'complex':
                    return 'complex'
                elif level == 'medium':
                    return 'medium'
        
        return 'simple'
    
    def _identify_missing_techniques(self, prompt: str) -> List[str]:
        """Identify which core techniques are missing."""
        missing = []
        
        # Check for examples
        if not ('example' in prompt.lower() or re.search(r'input.*output', prompt, re.IGNORECASE)):
            missing.append('use_examples')
            
        # Check for XML structure
        if not re.search(r'<\w+>', prompt):
            missing.append('xml_tags')
            
        # Check for role
        if not re.search(r'you are|act as|role', prompt, re.IGNORECASE):
            missing.append('role_prompting')
            
        # Check for thinking instructions
        if not re.search(r'think|reason|analyze|consider', prompt, re.IGNORECASE):
            missing.append('chain_of_thought')
            
        return missing
    
    def _generate_recommendations(self, analysis: Dict, prompt: str) -> List[str]:
        """Generate specific recommendations based on analysis."""
        recommendations = []
        
        if analysis["clarity_score"] < 6:
            recommendations.append("Add clear context, audience, and success criteria")
            
        if analysis["structure_score"] < 6:
            recommendations.append("Structure with XML tags for better organization")
            
        if "use_examples" in analysis["missing_techniques"]:
            recommendations.append("Add 3-5 diverse examples to show desired format")
            
        if "chain_of_thought" in analysis["missing_techniques"] and analysis["complexity_level"] != "simple":
            recommendations.append("Add chain of thought for systematic reasoning")
            
        if "role_prompting" in analysis["missing_techniques"]:
            recommendations.append("Specify expert role for domain knowledge")
            
        if analysis["complexity_level"] == "complex":
            recommendations.append("Consider breaking into multiple chained prompts")
            
        return recommendations

def main():
    """CLI interface for prompt analysis."""
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python prompt_analyzer.py '<prompt_text>'")
        sys.exit(1)
        
    prompt = sys.argv[1]
    analyzer = PromptAnalyzer()
    analysis = analyzer.analyze_prompt(prompt)
    
    print("=== PROMPT ANALYSIS ===")
    print(f"Clarity Score: {analysis['clarity_score']}/10")
    print(f"Structure Score: {analysis['structure_score']}/10") 
    print(f"Complexity Level: {analysis['complexity_level']}")
    print(f"Missing Techniques: {', '.join(analysis['missing_techniques'])}")
    print("\n=== RECOMMENDATIONS ===")
    for i, rec in enumerate(analysis['recommendations'], 1):
        print(f"{i}. {rec}")

if __name__ == "__main__":
    main()
