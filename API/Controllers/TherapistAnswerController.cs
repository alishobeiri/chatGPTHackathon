using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json;
using System.Threading.Tasks;
using API.Services;
using Microsoft.AspNetCore.Mvc;

namespace API.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class TherapistAnswerController : ControllerBase
    {
        // public AiscriptsServices AiscriptsServices { get; set; }

        // public TherapistAnswerController(AiscriptsServices aiscriptsServices)
        // {
        //     AiscriptsServices = aiscriptsServices;
        // }
        //FIX the dependency injection

        [HttpGet]
        public string GetTherapistAnswers()
        {
            // var result = AiscriptsServices.Experiment1("Therapist Answerss 2");
            var result = Experiment1("Therapist Answerss 2");   
            return JsonSerializer.Serialize(result);

        }

        [HttpGet("{id}")]

        public string GetTherapistAnswer(int id)
        {
            return "Therapist Answer";
        }

        public string Experiment1(string x)
        {
            // 1) Create Process
            var psi = new System.Diagnostics.ProcessStartInfo();
            psi.FileName = @"/Applications/Python 3.11/Python Launcher.app";
            // psi.Arguments = @"/Users/robert/Projects/aiscripts/FirstVersion.py";

            // 2) Provide scripts and arguments
            var script =  @"/Users/robert/Projects/aiscripts/FirstVersion.py";
            var prompt = "Say this is a test but as a joke";
            psi.Arguments = $"\"{script}\" \"{prompt}\"\"";
            // 3) Process configuration
            psi.UseShellExecute = false;
            psi.RedirectStandardOutput = true;
            psi.RedirectStandardError = true;
            psi.CreateNoWindow = true;

            // 4) Start process
            var errors = "";
            var results = "";
            using (var process = System.Diagnostics.Process.Start(psi))
            {
                errors = process.StandardError.ReadToEnd();
                results = process.StandardOutput.ReadToEnd();
            }
            // 5) Display output
            if (errors != "")
            {
                return errors;
            }
            return results;
        }

    }
}