import unittest
from main import loo

class TestTranslation(unittest.TestCase):
    def test_translation(self):
        test_cases = {
            'กิน' : 'ลินกุน',
            'ใช่' : 'ใล่ชุ่ย',
            'แมว' : 'แลวมูว',
            'ขำ' : 'หลำขุม',
            'ผัว' : 'หลัวผูว',
            'ซื้อ' : 'ลื้อซู้ว',
            'กระดาษ' : 'หละกุหลาษดูษ',
            'ไปกับใคร' : 'ไลปุยหลับกุบใลครุย',
            'รัก' : 'ซักรุก',
            'เหลือ' : 'เสือหลู',
            'ลอง' : 'ซองลูง',
            'รั่ว' : 'ซั่วรุ่ว',
            'ร้อน' : 'ซ้อนรู้น',
            'ลม' : 'ซมลุม',
            'กู' : 'ลูกี',
            'บูด' : 'หลูดบี',
            'สูบ' : 'หลูบสีบ',
            'บุญ' : 'ลุญบิญ',
            'รู้' : 'ซู้รี้',
            'ลูบ' : 'ซู่บลีป',
            'รุม' : 'ซุมริม',
            'ควย' : 'ลวยคุย',
            'สยาม' : 'หละสุหลามหยูม',
            'ขโมย' : 'หละขุโลยมุย',
            'อยากโดนเย็ด' : 'หลากอยูกโลนดุนเล็ดยุด',
            'กินยำมั้ยลูก' : 'ลินกุนลำยุมลั้ยมุ้ยซูกลีก',
            'โยชิมาทำไม' : 'โลยูลิชูลามูลำทุมไลมุย',
            'ปังมากพี่นัด' : 'ลังปุงลากมูกลี่พู่ลัดนุด',
            'แคทเทอรีนยิงมัน' : 'แลทคูทเลอทูซีนลูนลิงยุงลันมุน',
            'โยชิมาทำไม' : 'โลยูลิชูลามูลำทุมไลมุย', 
            'แสลง':'หละสุแสงหลูง', 
            'ไบรอัน':'ไลรบุรลันอุน', 
            'อิดอกหิวว่ะอยากแดกหมูกะทะ':'ลิอุหลอกดูกหลิวหุวหละหวุหลากอยูกแหลกดูกหลูหมูละกุละทุ'
        }

        for input_text, expected_output in test_cases.items():
            translated_text = loo(input_text)
            self.assertEqual(translated_text, expected_output)
            
if __name__ == "__main__": 
    unittest.main()
    # Print the test results
    test_result = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestTranslation))
    print(test_result)

