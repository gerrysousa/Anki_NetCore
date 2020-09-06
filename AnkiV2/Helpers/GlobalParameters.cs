using System;
using System.Collections.Generic;
using System.Text;

namespace AnkiV2.Helpers
{
    public static class GlobalParameters
    {
        //---Config geral
        public static string CONFIG_REPORT_NAME = BuilderJson.ReturnParameterAppSettings("CONFIG_REPORT_NAME");
        public static string CONFIG_DEFAULT_APPLICATION_URL = BuilderJson.ReturnParameterAppSettings("CONFIG_DEFAULT_APPLICATION_URL");
        public static string CONFIG_GET_SCREENSHOT_FOR_EACH_STEP = BuilderJson.ReturnParameterAppSettings("CONFIG_GET_SCREENSHOT_FOR_EACH_STEP");
        public static int CONFIG_DEFAULT_TIMEOUT_IN_SECONDS = Int32.Parse(BuilderJson.ReturnParameterAppSettings("CONFIG_DEFAULT_TIMEOUT_IN_SECONDS"));
        public static string CONFIG_EXECUTION = BuilderJson.ReturnParameterAppSettings("CONFIG_EXECUTION");
        public static string CONFIG_BROWSER = BuilderJson.ReturnParameterAppSettings("CONFIG_BROWSER");
        public static bool CONFIG_BROWSER_HEADLESS = bool.Parse(BuilderJson.ReturnParameterAppSettings("CONFIG_BROWSER_HEADLESS"));
        public static string CONFIG_SELENIUM_HUB = BuilderJson.ReturnParameterAppSettings("CONFIG_SELENIUM_HUB");
        public static string CONFIG_PATH_DEBUG_NET_CORE = BuilderJson.ReturnParameterAppSettings("CONFIG_PATH_DEBUG_NET_CORE");

        public static string DB_URL = BuilderJson.ReturnParameterAppSettings("DB_URL");
        public static string DB_PORT = BuilderJson.ReturnParameterAppSettings("DB_PORT");
        public static string DB_NAME = BuilderJson.ReturnParameterAppSettings("DB_NAME");
        public static string DB_USER = BuilderJson.ReturnParameterAppSettings("DB_USER");
        public static string DB_PASSWORD = BuilderJson.ReturnParameterAppSettings("DB_PASSWORD");
        public static int DB_CONNECTION_TIMEOUT = Int32.Parse(BuilderJson.ReturnParameterAppSettings("DB_CONNECTION_TIMEOUT"));

        public static string ANKI_USUARIO = BuilderJson.ReturnParameterAppSettings("ANKI_USUARIO");
        public static string ANKI_SENHA = BuilderJson.ReturnParameterAppSettings("ANKI_SENHA");
        
            
    }
}

