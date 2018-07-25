# https://blog.csdn.net/houyanhua1/article/details/78119195 语音识别框架
# https://www.sohu.com/a/225189232_99922036  python调用语音模块时，
#    遇见TypeError:NoneType takes no arguments这种错误类型该如何解决

from win32com.client import constants
import os
import win32com.client
import pythoncom

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
        if s == '记事本':
            os.system('notepad')

if __name__ == '__main__':
    wordsToAdd = ["关机", "取消关机", "记事本", "画图板", "写字板", "设置", "关闭记事本" ]
    speechReco = SpeechRecognition(wordsToAdd)
    while True:
        pythoncom.PumpWaitingMessages()






