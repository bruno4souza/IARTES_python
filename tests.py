import  smatphone as sm


class TestSmartphone(object):
    def testmodelo (self):
        celular = sm.Smartphone()
        celular.set_modelo("Fold")
        celular.set_ano("2022")
        assert celular.liga() == True

    def testDobrar (self):
        celular = sm.Samsungfold()
        celular.set_modelo("Fold")
        celular.set_ano("2022")
        assert celular.dobrar() == True
