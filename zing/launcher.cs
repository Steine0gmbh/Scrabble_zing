// Portabler Starter für das Zing-Wortspiel.
// Das Spiel (zing.html) steckt als Ressource in der EXE, wird in einen festen Ordner
// entpackt (damit Highscore und Einstellungen erhalten bleiben) und im Edge-App-Fenster geöffnet.
using System;
using System.Diagnostics;
using System.IO;
using System.Reflection;
using System.Windows.Forms;

[assembly: AssemblyTitle("Zing Wortspiel")]
[assembly: AssemblyProduct("Zing Wortspiel")]
[assembly: AssemblyVersion("1.0.0.0")]

static class Program
{
    [STAThread]
    static void Main()
    {
        try
        {
            string dir = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData), "ZingWortspiel");
            Directory.CreateDirectory(dir);
            string html = Path.Combine(dir, "zing.html");
            using (Stream src = Assembly.GetExecutingAssembly().GetManifestResourceStream("zing.html"))
            using (FileStream dst = File.Create(html))
                src.CopyTo(dst);

            string url = new Uri(html).AbsoluteUri;
            string edge = FindEdge();
            if (edge != null)
            {
                // Eigenes Profil: stört den normalen Edge nicht und behält den Highscore
                string profile = Path.Combine(dir, "profil");
                string args = "--app=\"" + url + "\" --user-data-dir=\"" + profile + "\"" +
                              " --window-size=1360,1000 --no-first-run --no-default-browser-check";
                Process.Start(new ProcessStartInfo(edge, args) { UseShellExecute = false });
            }
            else
            {
                Process.Start(new ProcessStartInfo(html) { UseShellExecute = true });
            }
        }
        catch (Exception e)
        {
            MessageBox.Show("Zing konnte nicht gestartet werden:\n" + e.Message, "Zing Wortspiel",
                MessageBoxButtons.OK, MessageBoxIcon.Error);
        }
    }

    static string FindEdge()
    {
        foreach (Environment.SpecialFolder f in new[] { Environment.SpecialFolder.ProgramFilesX86, Environment.SpecialFolder.ProgramFiles })
        {
            string p = Path.Combine(Environment.GetFolderPath(f), @"Microsoft\Edge\Application\msedge.exe");
            if (File.Exists(p)) return p;
        }
        return null;
    }
}
