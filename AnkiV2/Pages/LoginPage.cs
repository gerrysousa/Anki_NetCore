using AnkiV2.Bases;
using OpenQA.Selenium;

namespace AnkiV2.Pages
{
    public class LoginPage : PageBase
    {
        #region Mapping
        By txtEmail = By.Id("email");
        By txtSenha = By.Id("password");
        By btnLogin = By.XPath("//input[@value='Log in']");

        #endregion

        #region Actions
        public void PreencherEmail(string email)
        {
            SendKeysNoReport(txtEmail, email);
        }

        public void PreencherSenha(string senha)
        {
            SendKeysNoReport(txtSenha, senha);
        }

        public void ClicarBotaoLogin()
        {
            Click(btnLogin);
        }

        #endregion
    }
}