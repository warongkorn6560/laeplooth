import unittest
from main import loo

class TestTranslation(unittest.TestCase):
    def test_translation(self):
        test_cases = {
            'กิน' : 'ลินกุน',
            'ใช่' : 'ใล่ชุ่ย',
            'แมว' : 'แลวมูว',
            'ขำ' : 'หลำขุม',
            'ผัว' : 'หลัวผุว',
            'ซื้อ' : 'ลื้อซู้ว',
            'กระดาษ' : 'หละกรุหลาษดูษ',
            'ไปกับใคร' : 'ไลปุยหลับกุบใลครุย',
            'รัก' : 'ซักรุก',
            'เหลือ' : 'เสือหลู',
            'ลอง' : 'ซองลูง',
            'รั่ว' : 'ซั่วรุ่ว',
            'ร้อน' : 'ซ้อนรู้น',
            'ลม' : 'ซมลูม',
            'กู' : 'ลูกี',
            'บูด' : 'หลูดบีด',
            'สูบ' : 'หลูบสีบ',
            'บุญ' : 'ลุญบีญ',
            'รู้' : 'ซู้รี้้',
            'ลูบ' : 'ซูบลีบ',
            'รุม' : 'ซุมริม',
            'ควย' : 'ลวยคุย',
            'สยาม' : 'หละสุหลามหยูม',
            'ขโมย' : 'หละขุโลยมูย',
            'อยากโดนเย็ด' : 'หลากอยูกโลนดูนเล็ดยุด',
            'กินยำมั้ยลูก' : 'ลินกุนลำยุมลั้ยมุ้ยซูกลีก',
            'โยชิมาทำไม' : 'โลยูลิชุลามูลำทุมไลมุย',
            'ปังมากพี่นัด' : 'ลังปุงลากมูกลี่พู่ลัดนุด',
            'แคทเทอรีนยิงมัน' : 'แลทคูทเลอทูซีนรูนลิงยุงลันมุน',
            'แสลง':'หละสุแสงหลูง', 
            'ไบรอัน':'ไลรบุรลันอุน', 
            'อิดอกหิวว่ะอยากแดกหมูกะทะ':'หลิอุหลอกดูกหลิวหุวล่ะวุ่หลากอยูกแหลกดูกลูหมีหละกุละทุ'
        }

        for input_text, expected_output in test_cases.items():
            translated_text = loo(input_text)
            self.assertEqual(translated_text, expected_output)
            
if __name__ == "__main__": 
    unittest.main()
    # Print the test results
    test_result = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestTranslation))
    print(test_result)
