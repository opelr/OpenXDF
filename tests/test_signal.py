# -*- coding: utf-8 -*-

from .context import openxdf
import unittest


class Signal_Test(unittest.TestCase):
    """Test cases for the openxdf.signal module"""

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.xdf_path = "tests/data/test.xdf"
        self.signal_path = "tests/data/test.nkamp"
        self.xdf = openxdf.OpenXDF(self.xdf_path)

    def test_Signal(self):
        signal = openxdf.Signal(self.xdf, self.signal_path)
        assert type(signal) == openxdf.Signal
    
    def test_frame_information(self):
        signal = openxdf.Signal(self.xdf, self.signal_path)
        frame_info = signal._frame_information
        assert type(frame_info) is dict

        keys = ["FrameLength", "EpochLength", "FrameWidth", "Channels"]
        assert all([i in frame_info.keys() for i in keys])

    def test_parse(self):
        signal = openxdf.Signal(self.xdf, self.signal_path)
        signal_list = signal._parse()
        frame_info = signal._frame_information

        assert type(signal_list) is list
        assert len(signal_list[0].keys()) == len(frame_info["Channels"])

    def test_to_numeric(self):
        signal = openxdf.Signal(self.xdf, self.signal_path)
        numeric = signal.to_numeric(channels="FP1")

        assert type(numeric) is dict
        assert "FP1" in numeric.keys()

        total_epochs = max([i["EpochNumber"] for i in self.xdf.epochs])
        assert len(numeric["FP1"]) == total_epochs