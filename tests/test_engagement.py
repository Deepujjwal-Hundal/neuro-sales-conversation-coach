import unittest
from backend.src.engagement import calculate_engagement_score

class TestEngagementScore(unittest.TestCase):

    def test_engagement_score_basic(self):
        # Test with basic tone, loudness, and sentiment values
        tone_change = 0.5
        loudness_dynamics = 0.3
        sentiment_polarity = 0.2
        expected_score = (0.5 * tone_change) + (0.3 * loudness_dynamics) + (0.2 * sentiment_polarity)
        actual_score = calculate_engagement_score(tone_change, loudness_dynamics, sentiment_polarity)
        self.assertAlmostEqual(actual_score, expected_score, places=2)

    def test_engagement_score_zero_values(self):
        # Test with zero values for all parameters
        tone_change = 0.0
        loudness_dynamics = 0.0
        sentiment_polarity = 0.0
        expected_score = 0.0
        actual_score = calculate_engagement_score(tone_change, loudness_dynamics, sentiment_polarity)
        self.assertEqual(actual_score, expected_score)

    def test_engagement_score_extreme_values(self):
        # Test with extreme values for tone, loudness, and sentiment
        tone_change = 1.0
        loudness_dynamics = 1.0
        sentiment_polarity = 1.0
        expected_score = (0.5 * tone_change) + (0.3 * loudness_dynamics) + (0.2 * sentiment_polarity)
        actual_score = calculate_engagement_score(tone_change, loudness_dynamics, sentiment_polarity)
        self.assertAlmostEqual(actual_score, expected_score, places=2)

if __name__ == '__main__':
    unittest.main()