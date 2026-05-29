#!/usr/bin/env python3
"""
Quality Checker Script
Validates optimized prompts against best practices checklist.
"""

import re
from typing import Dict, List, Tuple

class QualityChecker:
    def __init__(self):
        self.quality_checks = [
            ("has_clear_task", "Contains clear task definition"),
            ("has_context", "Provides sufficient context"),
            ("has_examples", "Includes relevant examples"),
            ("has_xml_structure", "Uses XML tags for organization"),
            ("has_constraints", "Defines clear constraints"),
            ("has_output_format", "Specifies output format"),
            ("avoids_ambiguity", "Avoids ambiguous language"),
            ("appropriate_complexity", "Matches complexity to task")
        ]
    
    def validate_prompt(self, prompt: str) -> Dict:
        """Validate an optimized prompt against quality checklist."""
        results = {}
        
        for check_name, description in self.quality_checks:
            method = getattr(self, f"_check_{check_name}")
            results[check_name] = {
                "passed": method(prompt),
                "description": description
            }
        
        # Calculate overall score
        passed_count = sum(1 for result in results.values() if result["passed"])
        overall_score = (passed_count / len(self.quality_checks)) * 100
        
        return {
            "overall_score": overall_score,
            "checks": results,
            "recommendations": self._generate_quality_recommendations(results)
        }
    
    def _check_has_clear_task(self, prompt: str) -> bool:
        """Check if prompt has clear task definition."""
        task_indicators = ["task", "objective", "goal", "do", "create", "analyze", "write"]
        return any(indicator in prompt.lower() for indicator in task_indicators)
    
    def _check_has_context(self, prompt: str) -> bool:
        """Check if prompt provides context."""
        context_indicators = ["context", "background", "situation", "purpose", "for"]
        return any(indicator in prompt.lower() for indicator in context_indicators)
    
    def _check_has_examples(self, prompt: str) -> bool:
        """Check if prompt includes examples."""
        return bool(re.search(r'example|input.*output|<example>', prompt, re.IGNORECASE))
    
    def _check_has_xml_structure(self, prompt: str) -> bool:
        """Check if prompt uses XML tags."""
        return bool(re.search(r'<\w+>', prompt))
    
    def _check_has_constraints(self, prompt: str) -> bool:
        """Check if prompt defines constraints."""
        constraint_indicators = ["constraint", "requirement", "must", "should", "limit", "maximum", "minimum"]
        return any(indicator in prompt.lower() for indicator in constraint_indicators)
    
    def _check_has_output_format(self, prompt: str) -> bool:
        """Check if prompt specifies output format."""
        format_indicators = ["format", "structure", "organize", "present", "output"]
        return any(indicator in prompt.lower() for indicator in format_indicators)
    
    def _check_avoids_ambiguity(self, prompt: str) -> bool:
        """Check if prompt avoids ambiguous language."""
        ambiguous_terms = ["something", "anything", "stuff", "things", "whatever"]
        ambiguous_count = sum(prompt.lower().count(term) for term in ambiguous_terms)
        return ambiguous_count <= 1  # Allow minimal ambiguity
    
    def _check_appropriate_complexity(self, prompt: str) -> bool:
        """Check if prompt complexity matches task."""
        # Simple heuristic: longer prompts should have more structure
        word_count = len(prompt.split())
        xml_tags = len(re.findall(r'<\w+>', prompt))
        
        if word_count > 200:  # Long prompt should have structure
            return xml_tags >= 3
        elif word_count > 100:  # Medium prompt should have some structure
            return xml_tags >= 1
        else:  # Short prompt is fine as-is
            return True
    
    def _generate_quality_recommendations(self, results: Dict) -> List[str]:
        """Generate recommendations based on failed checks."""
        recommendations = []
        
        failed_checks = [name for name, result in results.items() if not result["passed"]]
        
        for check in failed_checks:
            if check == "has_clear_task":
                recommendations.append("Add explicit task definition using <task> tags")
            elif check == "has_context":
                recommendations.append("Provide background context and purpose")
            elif check == "has_examples":
                recommendations.append("Include 3-5 diverse examples showing desired format")
            elif check == "has_xml_structure":
                recommendations.append("Structure prompt with XML tags for clarity")
            elif check == "has_constraints":
                recommendations.append("Define clear constraints and requirements")
            elif check == "has_output_format":
                recommendations.append("Specify desired output format and structure")
            elif check == "avoids_ambiguity":
                recommendations.append("Replace vague terms with specific instructions")
            elif check == "appropriate_complexity":
                recommendations.append("Add more structure for complex prompts")
        
        return recommendations

def main():
    """CLI interface for quality checking."""
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python quality_checker.py '<prompt_text>'")
        sys.exit(1)
        
    prompt = sys.argv[1]
    checker = QualityChecker()
    validation = checker.validate_prompt(prompt)
    
    print("=== QUALITY VALIDATION ===")
    print(f"Overall Score: {validation['overall_score']:.1f}%")
    print("\n=== QUALITY CHECKS ===")
    
    for check_name, result in validation['checks'].items():
        status = "✅ PASS" if result["passed"] else "❌ FAIL"
        print(f"{status} {result['description']}")
    
    if validation['recommendations']:
        print("\n=== RECOMMENDATIONS ===")
        for i, rec in enumerate(validation['recommendations'], 1):
            print(f"{i}. {rec}")
    else:
        print("\n✅ All quality checks passed!")

if __name__ == "__main__":
    main()
