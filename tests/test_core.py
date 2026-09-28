import unittest, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from client import ConversationalBargeInArbitrator

class CoreTests(unittest.TestCase):
    def setUp(self):self.c=ConversationalBargeInArbitrator()

    def test_word_boundaries_and_silence(self):
        self.assertFalse(self.c.classify_utterance_intent('notebook')['is_command'])
        self.assertTrue(self.c.classify_utterance_intent('stop!')['is_command'])
        self.assertEqual(self.c.evaluate_interruption_event(True,-20,'',0.1,1000)['decision'],'AWAIT_CLARIFICATION')
        self.assertEqual(self.c.evaluate_interruption_event(True,-20,'mhm',0.1,250)['decision'],'ACKNOWLEDGE_BACKCHANNEL')
    def test_rollback_preserves_text(self):
        for ratio in [0,0.2,0.5,1]:
            text='Hello brave world'
            r=self.c.compute_playback_rollback_state(text,ratio)
            self.assertEqual(r['actually_heard_by_user']+r['truncated_unheard_text'],text)
        self.assertEqual(self.c.compute_playback_rollback_state('Hello world',1)['actually_heard_by_user'],'Hello world')
