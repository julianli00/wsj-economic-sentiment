# WSJ News Sentiment Annotation Agreement Study

## Overview
This study analyzes the inter-annotator agreement on sentiment annotations for WSJ news articles. The articles were annotated by multiple annotators using a 3-point scale:
- 1: Positive 
- 0: Neutral
- -1: Negative

## Data Statistics
### Overall Distribution
**Annotation 1:**
- Positive (1): 81 articles
- Neutral (0): 54 articles  
- Negative (-1): 65 articles

**Annotation 2:**
- Positive (1): 79 articles
- Neutral (0): 57 articles
- Negative (-1): 64 articles

### Agreement Analysis
- Overall Agreement Rate: 83.00%
- Average Difference (excluding matches): 1.0882
- Total Articles: 200

## Key Findings
1. High overall agreement (83%) between annotators indicates good reliability
2. When disagreements occur, they tend to be by about 1 point on the scale
3. Distribution of sentiment is relatively balanced across categories
4. Most common disagreements occur between:
   - Neutral vs Positive
   - Neutral vs Negative 
   - Rarely between Positive vs Negative

## Disagreement Analysis 
Main types of articles with annotator disagreements:

1. Economic policy articles (e.g. Fed decisions)
2. Market performance reports 
3. Articles with mixed sentiment indicators
4. Articles focused on specific sectors/indicators

## Recommendations
1. Clearer guidelines for:
   - Mixed sentiment articles
   - Policy impact assessment
   - Market movement thresholds
2. Additional training on ambiguous cases
3. Consider adding confidence scores for annotations
4. Potential refinement of the annotation scale

## Limitations
1. Binary sentiment may oversimplify complex economic news
2. Context dependence of interpretation
3. Temporal effects on sentiment assessment
4. Limited number of annotators