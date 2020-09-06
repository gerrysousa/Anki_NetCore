using AnkiV2.Helpers;
using NUnit.Framework;
using Castle.DynamicProxy;
using System.Collections.Generic;
using System.Reflection;

namespace AnkiV2.Bases
{
    public class TestBase
    {
        [OneTimeSetUp]
        public void OneTimeSetUp()
        {
            ExtentReportHelpers.CreateReport();
            DriverFactory.CreateInstance();
            ExtentReportHelpers.AddTest();
            DriverFactory.INSTANCE.Navigate().GoToUrl(GlobalParameters.CONFIG_DEFAULT_APPLICATION_URL);

            #region [AutoInstance] atribute methods calls to auto instace pages and flows
            //Necessário para realizar a instanciação automática das páginas e fluxos
            this.ProxyGenerator = new ProxyGenerator();
            InjectPageObjects(CollectPageObjects(), null);
            #endregion
        }

        [SetUp]
        public void Setup()
        {
            ExtentReportHelpers.AddTest();
        }

        [TearDown]
        public void TearDown()
        {
            ExtentReportHelpers.AddTestResult();
            ExtentReportHelpers.GenerateReport();
        }



        [OneTimeTearDown]
        public void OneTimeTearDown()
        {
            ExtentReportHelpers.GenerateReport();
            DriverFactory.QuitInstace();
        }

        #region Methodes needed to auto intance pages and flows [AutoInstance]
        //Esses métodos necessariamente precisam estar nesta classe, não funciona se estiverem em outro arquivo.
        private ProxyGenerator ProxyGenerator;

        private void InjectPageObjects(List<FieldInfo> fields, IInterceptor proxy)
        {
            foreach (FieldInfo field in fields)
            {
                field.SetValue(this, ProxyGenerator.CreateClassProxy(field.FieldType, proxy));
            }
        }

        private List<FieldInfo> CollectPageObjects()
        {
            List<FieldInfo> fields = new List<FieldInfo>();

            foreach (FieldInfo field in this.GetType().GetRuntimeFields())
            {
                if (field.GetCustomAttribute(typeof(AutoInstance)) != null)
                    fields.Add(field);
            }

            return fields;
        }
        #endregion
    }
}
