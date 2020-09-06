using AnkiV2.Bases;
using AnkiV2.Flows;
using AnkiV2.Helpers;
using AnkiV2.Pages;
using NUnit.Framework;
using System.Collections;
using System.Linq;
using System.Threading;

namespace AnkiV2.Tests
{
    class InserirFrasesTests : TestBase
    {
        #region Pages and Flows Objects       
        [AutoInstance] LoginPage loginPage;
        [AutoInstance] AreaLogadaPage areaLogadaPage;

        [OneTimeSetUp]
        public void OneTimeSetUp2()
        {
            loginPage.PreencherEmail(GlobalParameters.ANKI_USUARIO);
            loginPage.PreencherSenha(GlobalParameters.ANKI_SENHA);
            loginPage.ClicarBotaoLogin();

            areaLogadaPage.ClicarBotaoAdd();
        }

        #endregion

        #region Data Driven Providers
        public static IEnumerable ObterNovasFrases()
        {
            return GeneralHelpers.ReturnCSVData(GeneralHelpers.ReturnProjectPath() + "Resources/AnkiFrases.csv");
        }
        #endregion

        [Test, TestCaseSource("ObterNovasFrases")]
        public void InserirNovasFrasesTeste(ArrayList testData)
        {
            string front = testData[0].ToString();
            string back = testData[1].ToString();

            areaLogadaPage.EscreverFrontCard(front);
            areaLogadaPage.EscreverBackCard(back);
            areaLogadaPage.EscreverTagCard("Automatico_Sem_audio");
            areaLogadaPage.ClicarBotaoSalvar();
        }

    }
}