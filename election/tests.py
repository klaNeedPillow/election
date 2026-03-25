from django.test import TestCase, Client
from django.urls import reverse
from .models import Candidate, Vote

class ElectionFunctionalTest(TestCase):
    def setUp(self):
        # สร้างข้อมูลจำลองสำหรับทดสอบ
        self.candidate = Candidate.objects.create(number=1, name="นาย ก", policy="นโยบาย 1")
        self.client = Client()

    def test_vote_increases_count(self):
        # 1. เข้าหน้าโหวตของ user01
        url = reverse('vote', args=['user01', self.candidate.id])
        self.client.get(url)

        # 2. เช็คว่าใน DB มีคะแนนเพิ่มขึ้นจริงไหม
        vote_count = Vote.objects.filter(candidate=self.candidate).count()
        self.assertEqual(vote_count, 1)

    def test_prevent_double_voting(self):
        # 1. user01 โหวตครั้งแรก
        url = reverse('vote', args=['user01', self.candidate.id])
        self.client.get(url)
        
        # 2. user01 พยายามโหวตอีกรอบ (ระบบต้องไม่สร้างแถวใหม่ใน DB)
        self.client.get(url)
        
        vote_count = Vote.objects.filter(voter_name='user01').count()
        self.assertEqual(vote_count, 1) # ต้องยังคงเป็น 1 เท่านั้น