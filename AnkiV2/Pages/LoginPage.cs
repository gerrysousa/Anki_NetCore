using AnkiV2.Bases;
using OpenQA.Selenium;

namespace AnkiV2.Pages
{
    public class LoginPage : PageBase
    {
        #region Mapping
        // By txtEmail = By.Id("email");
        // By txtSenha = By.Id("password");
        // By btnLogin = By.XPath("//input[@value='Log in']");
        By txtEmail = By.XPath("//input[@placeholder='Email']");
        By txtSenha = By.XPath("//input[@placeholder='Password']");
        By btnLogin = By.XPath("//button[@class='btn btn-primary btn-lg']");


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