import unittest
import chunk_audio

class TestChunkAudio(unittest.TestCase):
    pass

    @classmethod
    def setUpClass(cls):
        cls.out_path = "./test/resources/temp"
        chunk_audio(filelist=["./test/resources/test_audio_12s.wav"], silence_len=800, silence_thr=-40, chunklen=1.5, training_len=5, out_path=cls.out_path)

    def test_number_of_files(self):
        self.assertEqual(len(os.listdir(self.out_path)), 2)

    @classmethod
    def tearDownClass(cls):
        for file in os.listdir(cls.out_path):
            os.remove(os.path.join(cls.out_path,file))