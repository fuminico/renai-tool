import React, { useState, useEffect } from 'react';
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Eye, Heart, Share2, RotateCcw } from 'lucide-react';
import './App.css';

function App() {
  const [questionsData, setQuestionsData] = useState([]);
  const [resultTypesData, setResultTypesData] = useState([]);
  const [currentScreen, setCurrentScreen] = useState('start'); // start, quiz, result
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [selectedQuestions, setSelectedQuestions] = useState([]);
  const [answers, setAnswers] = useState([]);
  const [totalScore, setTotalScore] = useState(0);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [questionsRes, resultsRes] = await Promise.all([
          fetch('questions.json'),
          fetch('result_types.json')
        ]);
        const questions = await questionsRes.json();
        const results = await resultsRes.json();
        setQuestionsData(questions);
        setResultTypesData(results);
        setLoading(false);
      } catch (error) {
        console.error("データの読み込みに失敗しました", error);
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  const selectRandomQuestions = () => {
    if (questionsData.length === 0) return [];
    const shuffled = [...questionsData].sort(() => 0.5 - Math.random());
    return shuffled.slice(0, 10);
  };

  const startQuiz = () => {
    const questions = selectRandomQuestions();
    setSelectedQuestions(questions);
    setCurrentQuestionIndex(0);
    setAnswers([]);
    setTotalScore(0);
    setCurrentScreen('quiz');
  };

  const selectAnswer = (choice) => {
    const newAnswers = [...answers, choice];
    const newScore = totalScore + choice.score;
    
    setAnswers(newAnswers);
    setTotalScore(newScore);

    if (currentQuestionIndex < selectedQuestions.length - 1) {
      setCurrentQuestionIndex(currentQuestionIndex + 1);
    } else {
      calculateResult(newScore);
    }
  };

  const calculateResult = (score) => {
    const normalizedScore = Math.max(20, Math.min(90, Math.round((score / 100) * 70 + 20)));
    
    const resultType = resultTypesData.find(type => 
      normalizedScore >= type.score_range[0] && normalizedScore <= type.score_range[1]
    );

    let coupleImage;
    if (normalizedScore >= 20 && normalizedScore <= 29) coupleImage = 'pict/couple_20_29.png';
    else if (normalizedScore <= 39) coupleImage = 'pict/couple_30_39.png';
    else if (normalizedScore <= 49) coupleImage = 'pict/couple_40_49.png';
    else if (normalizedScore <= 59) coupleImage = 'pict/couple_50_59.png';
    else if (normalizedScore <= 69) coupleImage = 'pict/couple_60_69.png';
    else if (normalizedScore <= 79) coupleImage = 'pict/couple_70_79.png';
    else if (normalizedScore <= 89) coupleImage = 'pict/couple_80_89.png';
    else coupleImage = 'pict/couple_90.png';

    setResult({
      score: normalizedScore,
      type: resultType?.type || 'タイプ不明',
      catchphrase: resultType?.catchphrase || '',
      advice: resultType?.advice || 'アドバイスが見つかりません',
      coupleImage: coupleImage
    });
    setCurrentScreen('result');
  };

  const restartQuiz = () => {
    setCurrentScreen('start');
    setResult(null);
  };

  const shareResult = (platform) => {
    const text = `私の恋愛偏差値は${result.score}でした！あなたも恋愛偏差値診断で自分の恋愛力をチェック！`;
    const url = window.location.href;
    
    if (platform === 'line') {
      window.open(`https://social-plugins.line.me/lineit/share?url=${encodeURIComponent(url)}&text=${encodeURIComponent(text)}`);
    } else if (platform === 'twitter') {
      window.open(`https://twitter.com/intent/tweet?text=${encodeURIComponent(text)}&url=${encodeURIComponent(url)}&hashtags=恋愛偏差値診断`);
    }
  };

  if (loading) {
    return <div className="app-container"><p>読み込み中...</p></div>;
  }

  return (
    <div className="app-container font-sans">
      <div className="main-content">
        {currentScreen === 'start' && (
          <Card className="start-card text-center p-8">
            <CardHeader>
              <div className="flex justify-center mb-6">
                <Eye className="w-20 h-20 text-yellow-300 floating-animation" />
              </div>
              <CardTitle className="text-5xl font-bold title-text mb-4">
                恋愛偏差値診断
              </CardTitle>
              <p className="text-lg text-indigo-200">
                あなたの恋愛における本当の実力を測定します
              </p>
            </CardHeader>
            <CardContent>
              <Button
                onClick={startQuiz}
                className="bg-yellow-500 hover:bg-yellow-600 text-gray-900 font-bold px-10 py-4 text-xl pulse-glow rounded-full"
              >
                <Heart className="w-6 h-6 mr-3" />
                診断を開始する
              </Button>
            </CardContent>
          </Card>
        )}

        {currentScreen === 'quiz' && selectedQuestions.length > 0 && (
          <Card className="quiz-card p-6">
            <CardHeader>
              <div className="flex justify-between items-center mb-4">
                <span className="text-indigo-300">
                  質問 {currentQuestionIndex + 1} / {selectedQuestions.length}
                </span>
                <div className="w-full bg-indigo-900 rounded-full h-2.5 ml-4">
                  <div
                    className="bg-yellow-400 h-2.5 rounded-full transition-all duration-300"
                    style={{ width: `${((currentQuestionIndex + 1) / selectedQuestions.length) * 100}%` }}
                  />
                </div>
              </div>
              <CardTitle className="text-2xl text-white pt-4">
                {selectedQuestions[currentQuestionIndex]?.question_text}
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {selectedQuestions[currentQuestionIndex]?.choices.map((choice, index) => (
                  <Button
                    key={index}
                    onClick={() => selectAnswer(choice)}
                    className="choice-button w-full p-4 h-auto text-lg rounded-lg"
                    variant="outline"
                  >
                    {choice.choice_text}
                  </Button>
                ))}
              </div>
            </CardContent>
          </Card>
        )}

        {currentScreen === 'result' && result && (
          <Card className="result-card p-6">
            <CardHeader className="text-center">
              <CardTitle className="text-4xl font-bold title-text mb-2">
                診断結果
              </CardTitle>
            </CardHeader>
            <CardContent className="text-center space-y-6">
              <div className="bg-indigo-900/50 rounded-lg p-6">
                <p className="text-xl text-indigo-200 mb-2">あなたの恋愛偏差値</p>
                <p className="text-8xl font-bold result-score mb-4">{result.score}</p>
                <p className="text-3xl font-semibold text-white mb-2">{result.type}</p>
                <p className="text-xl text-indigo-300 italic">「{result.catchphrase}」</p>
              </div>

              <div className="flex justify-center my-4">
                <img
                  src={result.coupleImage}
                  alt={`恋愛偏差値${result.score}のカップル`}
                  className="w-40 h-40 object-cover rounded-full border-4 border-yellow-400 shadow-lg"
                />
              </div>

              <div className="bg-indigo-900/30 rounded-lg p-6">
                <h3 className="text-2xl font-semibold text-white mb-3">あなたへのアドバイス</h3>
                <p className="text-indigo-100 leading-relaxed text-lg">{result.advice}</p>
              </div>

              <div className="flex flex-col sm:flex-row gap-4 justify-center">
                <Button onClick={() => shareResult('line')} className="bg-green-500 hover:bg-green-600 text-white font-bold text-base rounded-full">
                  <Share2 className="w-4 h-4 mr-2" />LINEでシェア
                </Button>
                <Button onClick={() => shareResult('twitter')} className="bg-sky-500 hover:bg-sky-600 text-white font-bold text-base rounded-full">
                  <Share2 className="w-4 h-4 mr-2" />Xでシェア
                </Button>
                <Button onClick={restartQuiz} className="bg-yellow-500 hover:bg-yellow-600 text-gray-900 font-bold text-base rounded-full">
                  <RotateCcw className="w-4 h-4 mr-2" />もう一度診断する
                </Button>
              </div>
            </CardContent>
          </Card>
        )}
      </div>
    </div>
  );
}

export default App;
