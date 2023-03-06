import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { switchMap } from 'rxjs/operators';
import { QuestionsService } from '../questions.service';
import { Quiz, Answers, Choice, Question } from '../quiz.model';

@Component({
  selector: 'app-questions',
  templateUrl: './questions.component.html',
  styleUrls: ['./questions.component.scss']
})
export class QuestionsComponent implements OnInit {

  quiz: Quiz;
  userSelectedIndex: number;
  questions: Question[];
  currentQuestionIndex: number;
  answer: string;
  userSelectedAnswer: string;

  showResults = false;
  // inject both the active route and the questions service
  constructor(private route: ActivatedRoute, private questionsService: QuestionsService) { }

  ngOnInit() {
    //read from the dynamic route and load the proper quiz data
    this.questionsService.getQuestions(this.route.snapshot.params.quizId)
      .subscribe(questions => {
        this.questions = questions;
        this.currentQuestionIndex = 0;
      });
  }

  updateChoice(choice: string) {
    this.userSelectedAnswer = choice;
    this.answer = this.questions[this.currentQuestionIndex].choices[this.questions[this.currentQuestionIndex].answer];
    this.userSelectedIndex = this.questions[this.currentQuestionIndex].choices.indexOf(choice)
  }

  nextOrViewResults() {
    if (this.showResults) {
      this.currentQuestionIndex++;
    }
    this.showResults = !this.showResults;

    if (this.currentQuestionIndex == this.questions.length) {
      this.questions = undefined;
      this.questionsService.getQuestions(this.route.snapshot.params.quizId)
      .subscribe(questions => {
        this.questions = questions;
        this.currentQuestionIndex = 0;
      });
    }
  }

  reset() {
    this.quiz = undefined;
    this.questions = undefined;
    this.userSelectedIndex = undefined;
    this.answer = undefined;
    this.currentQuestionIndex = undefined;
  }
}
