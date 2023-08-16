using AnkiV2.Bases;
using OpenQA.Selenium;
using System;

namespace AnkiV2.Pages
{
    public class AreaLogadaPage : PageBase
    {
        #region Mapping
        By txtFront =By.XPath("//div[span='Front']/div/div");//By.Id("f0");
        By txtBack = By.XPath("//div[span='Back']/div/div");//By.Id("f1");
        By txtTag = By.XPath("//div[span='Tags']/div/input");//By.Id("f-1");
        By btnSalvar = By.XPath("//button[text()='Add']");
        By btnAdd = By.XPath("//a[text()='Add']");
        By msgAddSucesso = By.Id("msg");
        By msgAddSucessoOculta = By.XPath("//div[@id='msg' and @style='display: none;']");

        #endregion

        #region Actions
        public void EscreverFrontCard(string front)
        {
            SendKeys(txtFront, front);
        }

        public void EscreverBackCard(string back)
        {
            SendKeys(txtBack, back);
        }

        public void EscreverTagCard(string tag)
        {
            SendKeys(txtTag, tag);
        }

        public void ClicarBotaoSalvar()
        {
            Click(btnSalvar);
        }

        public void ClicarBotaoAdd()
        {
            Click(btnAdd);
        }

        public bool VerificaSeExisteMensagemSucesso()
        {
            bool exite = ReturnIfElementIsDisplayed(msgAddSucesso);
            return exite;
        }

        #endregion
    }
}
