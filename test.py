import unittest

from funciones import SubPalindroma
from app import app

class TestFlaskPalindromo(unittest.TestCase):
    
    #PRUEBA A LA FUNCION Subcadena Palindroma
    def test_SubcadenaPalindroa_Pasa(self):
        self.assertEqual(SubPalindroma('irerq'), 'RER')

    def test_SubcadenaPalindroa_2Pasa(self):
        self.assertEqual(SubPalindroma('47ana ojo ana f47'), '4ANAOJOANA4')

    def test_SubcadenaPalindroa_3Pasa(self):
        self.assertEqual(SubPalindroma('qwer1235321fr'), 'R1235321R')

    def test_SubcadenaPalindroa_4NoPasa(self):
        self.assertNotEqual(SubPalindroma('qwer1235321fr'), '0')
        
    #VERIFICACION DEL API
    def test_home(self):  # VERIFICACION DEL QUE RENDEREADO SEA CORRECTO
        tester= app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
    #SUMINISTRO DE DATOS BAJO EL METODO POST
    def test_APISendCadena_1Pasa(self): 
        tester= app.test_client(self)
        response = tester.post('/', data = dict(cadena = 'irerq'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'RER', response.data)
    
    def test_APISendCadena_2NoPasa(self): 
        tester= app.test_client(self)
        response = tester.post('/', data = dict(cadena = 'irerq'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'0', response.data)
        
    def test_APISendCadena_3NoPasa(self):
        tester = app.test_client(self)
        response = tester.post('/', data=dict(cadena='an'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'A', response.data) 


if  __name__ == "__main__":
    unittest.main()
