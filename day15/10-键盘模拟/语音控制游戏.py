from win32com.client import constants
import win32com.client
import win32con
import pythoncom
import win32api
import time

class SpeechRecognition:
    def __init__(self, wordsToAdd):
        self.speaker = win32com.client.Dispatch("SAPI.SpVoice")
        self.listener = win32com.client.Dispatch("SAPI.SpSharedRecognizer")
        self.context = self.listener.CreateRecoContext()
        self.grammar = self.context.CreateGrammar()
        self.grammar.DictationSetState(0)
        self.wordsRule = self.grammar.Rules.Add("wordsRule", constants.SRATopLevel + constants.SRADynamic, 0)
        self.wordsRule.Clear()
        [self.wordsRule.InitialState.AddWordTransition(None, word) for word in wordsToAdd]
        self.grammar.Rules.Commit()
        self.grammar.CmdSetRuleState("wordsRule", 1)
        self.grammar.Rules.Commit()
        self.eventHandler = ContextEvents(self.context)
        self.say("Started successfully")
    def say(self, phrase):
        self.speaker.Speak(phrase)
class ContextEvents(win32com.client.getevents("SAPI.SpSharedRecoContext")):
    def OnRecognition(self, StreamNumber, StreamPosition, RecognitionType, Result):
        newResult = win32com.client.Dispatch(Result)
        print("说 ", newResult.PhraseInfo.GetText())
        s = newResult.PhraseInfo.GetText()
        if s == '上':
            win32api.keybd_event(38, 0, 0, 0)
            time.sleep(0.1)
            win32api.keybd_event(38, 0, win32con.KEYEVENTF_KEYUP, 0)
        elif s == '下':
            win32api.keybd_event(40, 0, 0, 0)
            time.sleep(0.1)
            win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)
        elif s == '左':
            win32api.keybd_event(37, 0, 0, 0)
            time.sleep(0.1)
            win32api.keybd_event(37, 0, win32con.KEYEVENTF_KEYUP, 0)
        elif s == '右':
            win32api.keybd_event(39, 0, 0, 0)
            time.sleep(0.1)
            win32api.keybd_event(39, 0, win32con.KEYEVENTF_KEYUP, 0)
        elif s == '打':
            win32api.keybd_event(32, 0, 0, 0)
            time.sleep(0.1)
            win32api.keybd_event(32, 0, win32con.KEYEVENTF_KEYUP, 0)

# http://www.7k7k.com/swf/77087.htm
if __name__ == '__main__':
    wordsToAdd = ['上', '下', '左', '右', '打']
    speechReco = SpeechRecognition(wordsToAdd)
    while True:
        pythoncom.PumpWaitingMessages()
