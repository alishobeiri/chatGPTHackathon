//define, what'll be used later on
import { Injectable } from '@angular/core';
import { HttpClient} from '@angular/common/http';
import { map } from 'rxjs/operators';
import { Quiz, Question } from './quiz.model';

// @Injectable decorator (function that augments a piece of code)
// tells Angular that this service will be available everywhere
@Injectable({
  providedIn: 'root'
})
export class QuestionsService {
  public loading: boolean;
  // contains namespace and type;
  //shortcut for: constructor(http: HttpClient){this.http = http;}
  constructor(private http: HttpClient) {
   }

  public getQuestions(fileName: string) {
    this.loading = true;
    var url = "http://127.0.0.1:8000/Ap-Bio-Curriculum";
    return this.http.get(`${url}`).pipe(
      map((result: any) => {
        this.loading = false;
        console.log(result);
        let questions = JSON.parse(result.choices[0].message.content).questions;
        return questions.map(question => new Question(question.question, question.choices, question.correct_choice, question.answer));
      })
    );
  }
}
