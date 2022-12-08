# coding: UTF-8
import Adafruit_PCA9685
import time
from loguru import logger

class ServoClass:
    #ChannelはPCA9685のサーボモータの接続チャンネル
    #ZeroOffsetはサーボモータの基準位置調節用パラメータ
    def __init__(self, Channel, ZeroOffset):
        self.Channel = Channel
        self.ZeroOffset = ZeroOffset

        #Adafruit_PCA9685の初期化
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(int(60))

    # 角度設定
    def SetPos(self, pos):
        #PCA9685はパルスで角度を制御しており、パルス150~650が角度0~180に対応
        pulse = int((650-150)/180*pos+150+self.ZeroOffset)
        self.pwm.set_pwm(self.Channel, 0, pulse)
        logger.info("deg : {}".format(pos))

    # pulse 設定
    def SetPulse(self, pulse):
        self.pwm.set_pwm(self.Channel, 0, pulse)
        
    # 終了処理
    def Cleanup(self):
        #サーボを90°にセット
        # self.SetPos(int(90))
        self.SetPos(0)
        logger.info("SetPos 0")

if __name__ == '__main__':
    Servo0 = ServoClass(Channel=0, ZeroOffset=0)
    
    try:
        while True:
                        
            for deg in range(180) :
                Servo0.SetPos(int(deg*2))
                logger.info("deg : {}".format(deg*2))
                time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nCtl+C")
    except Exception as e:
        print(str(e))
    finally:
        Servo0.Cleanup()

        print("\nexit program")