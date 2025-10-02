
import json
import random

def generate_question_and_choices(id_num):
    questions_data = [
        {
            "question_text": "初対面の人と話すとき、あなたはどのような態度をとりますか？",
            "choices": [
                {"choice_text": "積極的に話題を振って場を盛り上げる", "score": 10},
                {"choice_text": "相手の話を聞きながら、適度に相槌を打ち、共感を示す", "score": 7},
                {"choice_text": "相手が話しかけてくるのを待ち、必要最低限の返答をする", "score": 4},
                {"choice_text": "できるだけ会話を避け、目立たないようにする", "score": 1}
            ]
        },
        {
            "question_text": "気になる相手との初めてのデート、どんな場所を選びますか？",
            "choices": [
                {"choice_text": "話題のレストランやイベントなど、刺激的な場所", "score": 10},
                {"choice_text": "カフェや公園など、落ち着いて話せる場所", "score": 7},
                {"choice_text": "相手の好みを事前にリサーチし、それに合わせる", "score": 4},
                {"choice_text": "どこでもいいと相手に任せる", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの意見の相違があった場合、どう解決しますか？",
            "choices": [
                {"choice_text": "自分の意見をはっきり伝え、相手を説得する", "score": 10},
                {"choice_text": "お互いの意見を尊重し、納得できるまで話し合う", "score": 7},
                {"choice_text": "相手の意見を優先し、自分の意見は抑える", "score": 4},
                {"choice_text": "議論を避け、時間をおいて自然消滅を待つ", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、最も重要だと感じることは何ですか？",
            "choices": [
                {"choice_text": "情熱的な愛情表現と刺激的な関係", "score": 10},
                {"choice_text": "信頼と安心感、そして穏やかな日常", "score": 7},
                {"choice_text": "お互いの成長を促し、高め合える関係", "score": 4},
                {"choice_text": "経済的な安定と将来性", "score": 1}
            ]
        },
        {
            "question_text": "失恋したとき、どのように立ち直りますか？",
            "choices": [
                {"choice_text": "すぐに新しい出会いを求め、前向きに進む", "score": 10},
                {"choice_text": "友人に話を聞いてもらい、時間をかけて癒す", "score": 7},
                {"choice_text": "一人で静かに過ごし、自分と向き合う", "score": 4},
                {"choice_text": "仕事や趣味に没頭し、恋愛から距離を置く", "score": 1}
            ]
        },
        {
            "question_text": "友人が恋愛相談をしてきたら、どのようにアドバイスしますか？",
            "choices": [
                {"choice_text": "具体的な解決策を提示し、積極的にサポートする", "score": 10},
                {"choice_text": "共感を示し、じっくり話を聞いてあげる", "score": 7},
                {"choice_text": "客観的な視点から、冷静な意見を伝える", "score": 4},
                {"choice_text": "相手の決断を尊重し、見守る", "score": 1}
            ]
        },
        {
            "question_text": "理想のパートナー像について、最も重視する点は何ですか？",
            "choices": [
                {"choice_text": "外見の魅力とカリスマ性", "score": 10},
                {"choice_text": "内面の優しさと思いやりの心", "score": 7},
                {"choice_text": "共通の趣味や価値観", "score": 4},
                {"choice_text": "安定した職業と経済力", "score": 1}
            ]
        },
        {
            "question_text": "SNSでの恋愛関係の投稿について、どう思いますか？",
            "choices": [
                {"choice_text": "積極的に投稿し、幸せを共有したい", "score": 10},
                {"choice_text": "適度に投稿し、プライベートも大切にしたい", "score": 7},
                {"choice_text": "ほとんど投稿せず、個人的なものと考える", "score": 4},
                {"choice_text": "一切投稿せず、SNSとは切り離したい", "score": 1}
            ]
        },
        {
            "question_text": "サプライズを仕掛ける側と、される側、どちらが好きですか？",
            "choices": [
                {"choice_text": "仕掛ける側。相手の喜ぶ顔を見るのが好き", "score": 10},
                {"choice_text": "される側。予想外の出来事に感動したい", "score": 7},
                {"choice_text": "どちらでもない。特別なことはしなくていい", "score": 4},
                {"choice_text": "サプライズは苦手。事前に計画したい", "score": 1}
            ]
        },
        {
            "question_text": "パートナーの浮気を疑った場合、どう行動しますか？",
            "choices": [
                {"choice_text": "直接問い詰め、真実を明らかにする", "score": 10},
                {"choice_text": "冷静に状況を観察し、証拠を集める", "score": 7},
                {"choice_text": "友人に相談し、アドバイスを求める", "score": 4},
                {"choice_text": "見て見ぬふりをして、関係を続ける", "score": 1}
            ]
        },
        {
            "question_text": "恋愛と仕事、どちらを優先しますか？",
            "choices": [
                {"choice_text": "恋愛。仕事よりもパートナーとの時間を大切にしたい", "score": 10},
                {"choice_text": "状況による。バランスを重視する", "score": 7},
                {"choice_text": "仕事。キャリアを築くことが最優先", "score": 4},
                {"choice_text": "どちらも優先しない。自分の時間を大切にしたい", "score": 1}
            ]
        },
        {
            "question_text": "結婚について、どのような考えを持っていますか？",
            "choices": [
                {"choice_text": "運命の人と出会えればすぐにでもしたい", "score": 10},
                {"choice_text": "いつかはしたいが、焦る必要はない", "score": 7},
                {"choice_text": "あまり考えていない。成り行きに任せる", "score": 4},
                {"choice_text": "したくない。自由でいたい", "score": 1}
            ]
        },
        {
            "question_text": "パートナーの家族や友人との関係をどのように築きますか？",
            "choices": [
                {"choice_text": "積極的に交流し、良好な関係を築く", "score": 10},
                {"choice_text": "礼儀正しく接し、適度な距離を保つ", "score": 7},
                {"choice_text": "パートナーに任せ、自分からはあまり関わらない", "score": 4},
                {"choice_text": "必要であれば関わるが、基本的には避けたい", "score": 1}
            ]
        },
        {
            "question_text": "自分の感情をパートナーに伝えるのは得意ですか？",
            "choices": [
                {"choice_text": "得意。思ったことはすぐに伝える", "score": 10},
                {"choice_text": "ある程度は得意。伝え方には気を使う", "score": 7},
                {"choice_text": "苦手。なかなか言葉にできない", "score": 4},
                {"choice_text": "非常に苦手。感情を隠してしまう", "score": 1}
            ]
        },
        {
            "question_text": "パートナーに求める「癒し」とは具体的にどんなことですか？",
            "choices": [
                {"choice_text": "一緒にいるだけで心が安らぐ存在", "score": 10},
                {"choice_text": "悩みを聞いてくれ、励ましてくれること", "score": 7},
                {"choice_text": "美味しい食事を作ってくれること", "score": 4},
                {"choice_text": "何も言わずにそばにいてくれること", "score": 1}
            ]
        },
        {
            "question_text": "記念日をどのように祝いますか？",
            "choices": [
                {"choice_text": "豪華なディナーや旅行を計画する", "score": 10},
                {"choice_text": "手作りのプレゼントやメッセージで気持ちを伝える", "score": 7},
                {"choice_text": "普段より少し贅沢な食事をする", "score": 4},
                {"choice_text": "特に何もしない。普段通りでいい", "score": 1}
            ]
        },
        {
            "question_text": "パートナーの趣味に興味がない場合、どう対応しますか？",
            "choices": [
                {"choice_text": "積極的に参加し、一緒に楽しむ努力をする", "score": 10},
                {"choice_text": "理解を示し、話を聞いてあげる", "score": 7},
                {"choice_text": "特に何もせず、相手に任せる", "score": 4},
                {"choice_text": "自分の趣味を優先し、相手の趣味には関わらない", "score": 1}
            ]
        },
        {
            "question_text": "恋愛における「駆け引き」についてどう思いますか？",
            "choices": [
                {"choice_text": "必要。関係を盛り上げるスパイスになる", "score": 10},
                {"choice_text": "多少は必要。相手の気持ちを確かめるために", "score": 7},
                {"choice_text": "不要。素直な気持ちで向き合いたい", "score": 4},
                {"choice_text": "嫌い。疲れるだけ", "score": 1}
            ]
        },
        {
            "question_text": "遠距離恋愛について、どう思いますか？",
            "choices": [
                {"choice_text": "愛があれば乗り越えられる", "score": 10},
                {"choice_text": "努力は必要だが、不可能ではない", "score": 7},
                {"choice_text": "難しい。不安が大きい", "score": 4},
                {"choice_text": "無理。近くにいないと意味がない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーの過去の恋愛について、どこまで知りたいですか？",
            "choices": [
                {"choice_text": "全て知りたい。隠し事はなし", "score": 10},
                {"choice_text": "聞かれたら話す程度。深入りはしない", "score": 7},
                {"choice_text": "聞きたくない。過去は過去", "score": 4},
                {"choice_text": "全く興味がない", "score": 1}
            ]
        },
        {
            "question_text": "自分の弱みをパートナーに見せることはできますか？",
            "choices": [
                {"choice_text": "できる。それが真の信頼関係", "score": 10},
                {"choice_text": "ある程度はできる。相手を選ぶ", "score": 7},
                {"choice_text": "苦手。強い自分を見せたい", "score": 4},
                {"choice_text": "できない。弱みを見せるのは恥ずかしい", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの喧嘩の後、どう仲直りしますか？",
            "choices": [
                {"choice_text": "自分から謝り、解決策を話し合う", "score": 10},
                {"choice_text": "相手が謝ってくるのを待つ", "score": 7},
                {"choice_text": "時間をおいて、自然に仲直りする", "score": 4},
                {"choice_text": "喧嘩はしないように努力する", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、嫉妬心を感じやすいですか？",
            "choices": [
                {"choice_text": "感じやすい。独占欲が強い", "score": 10},
                {"choice_text": "たまに感じる。不安な時だけ", "score": 7},
                {"choice_text": "あまり感じない。相手を信頼している", "score": 4},
                {"choice_text": "全く感じない。無関心", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの将来について、どの程度具体的に考えますか？",
            "choices": [
                {"choice_text": "結婚や子育てまで具体的に計画している", "score": 10},
                {"choice_text": "漠然と考えているが、まだ具体的な計画はない", "score": 7},
                {"choice_text": "あまり考えていない。今が楽しければいい", "score": 4},
                {"choice_text": "全く考えていない", "score": 1}
            ]
        },
        {
            "question_text": "恋愛関係において、最も避けたい状況は何ですか？",
            "choices": [
                {"choice_text": "裏切りや浮気", "score": 10},
                {"choice_text": "すれ違いや誤解", "score": 7},
                {"choice_text": "マンネリ化", "score": 4},
                {"choice_text": "束縛されること", "score": 1}
            ]
        },
        {
            "question_text": "パートナーに感謝の気持ちを伝える頻度は？",
            "choices": [
                {"choice_text": "毎日、言葉や行動で伝える", "score": 10},
                {"choice_text": "気が向いた時に伝える", "score": 7},
                {"choice_text": "あまり伝えない。言わなくてもわかるはず", "score": 4},
                {"choice_text": "全く伝えない", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、自分から積極的にアプローチするタイプですか？",
            "choices": [
                {"choice_text": "はい、常に自分から行動します", "score": 10},
                {"choice_text": "相手の出方を見てから行動します", "score": 7},
                {"choice_text": "いいえ、相手からのアプローチを待ちます", "score": 4},
                {"choice_text": "恋愛自体に興味がありません", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの旅行、どんな計画を立てますか？",
            "choices": [
                {"choice_text": "全て自分で計画し、サプライズを盛り込む", "score": 10},
                {"choice_text": "二人で相談し、お互いの希望を叶える", "score": 7},
                {"choice_text": "相手に任せる", "score": 4},
                {"choice_text": "旅行にはあまり興味がない", "score": 1}
            ]
        },
        {
            "question_text": "恋愛における「束縛」についてどう思いますか？",
            "choices": [
                {"choice_text": "愛の証。多少はあってもいい", "score": 10},
                {"choice_text": "度が過ぎなければ許容できる", "score": 7},
                {"choice_text": "苦手。自由でいたい", "score": 4},
                {"choice_text": "絶対に嫌。すぐに別れる", "score": 1}
            ]
        },
        {
            "question_text": "パートナーの成長をどのようにサポートしますか？",
            "choices": [
                {"choice_text": "目標達成のために、具体的なアドバイスや手助けをする", "score": 10},
                {"choice_text": "精神的に支え、励まし続ける", "score": 7},
                {"choice_text": "見守る。自分で乗り越える力を信じる", "score": 4},
                {"choice_text": "特に何もせず、相手に任せる", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、直感を信じるタイプですか？",
            "choices": [
                {"choice_text": "はい、直感を信じて行動します", "score": 10},
                {"choice_text": "ある程度は信じるが、最終的には論理的に考える", "score": 7},
                {"choice_text": "いいえ、直感よりも現実的な判断を重視する", "score": 4},
                {"choice_text": "全く信じない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの共通の友人は必要だと思いますか？",
            "choices": [
                {"choice_text": "はい、関係を深めるために必要", "score": 10},
                {"choice_text": "どちらでもいい。いなくても困らない", "score": 7},
                {"choice_text": "いいえ、二人だけの世界を大切にしたい", "score": 4},
                {"choice_text": "むしろいない方がいい", "score": 1}
            ]
        },
        {
            "question_text": "恋愛関係において、秘密は許されますか？",
            "choices": [
                {"choice_text": "いいえ、全てを共有すべき", "score": 10},
                {"choice_text": "内容による。相手を傷つけない秘密なら", "score": 7},
                {"choice_text": "はい、プライベートは尊重すべき", "score": 4},
                {"choice_text": "秘密はあって当然", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの金銭感覚の違い、どう対応しますか？",
            "choices": [
                {"choice_text": "話し合い、共通のルールを作る", "score": 10},
                {"choice_text": "お互いの価値観を尊重し、干渉しない", "score": 7},
                {"choice_text": "自分が合わせる", "score": 4},
                {"choice_text": "見て見ぬふりをする", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、ロマンチックな演出は重要だと思いますか？",
            "choices": [
                {"choice_text": "非常に重要。関係を盛り上げる", "score": 10},
                {"choice_text": "たまには必要。サプライズは好き", "score": 7},
                {"choice_text": "あまり重要ではない。日常が大切", "score": 4},
                {"choice_text": "不要。気恥ずかしい", "score": 1}
            ]
        },
        {
            "question_text": "パートナーの短所をどのように受け入れますか？",
            "choices": [
                {"choice_text": "長所として捉え、愛する", "score": 10},
                {"choice_text": "理解しようと努力する", "score": 7},
                {"choice_text": "指摘し、改善を促す", "score": 4},
                {"choice_text": "見て見ぬふりをする", "score": 1}
            ]
        },
        {
            "question_text": "恋愛における「運命」についてどう思いますか？",
            "choices": [
                {"choice_text": "運命を信じる。出会いは必然", "score": 10},
                {"choice_text": "信じたい気持ちはあるが、努力も必要", "score": 7},
                {"choice_text": "あまり信じない。努力が全て", "score": 4},
                {"choice_text": "全く信じない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も大切にしたいことは何ですか？",
            "choices": [
                {"choice_text": "深い愛情と信頼", "score": 10},
                {"choice_text": "お互いの自由と尊重", "score": 7},
                {"choice_text": "共通の目標や夢", "score": 4},
                {"choice_text": "経済的な安定", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、過去の経験から何を学びましたか？",
            "choices": [
                {"choice_text": "失敗から学び、次へと活かす", "score": 10},
                {"choice_text": "経験は経験として受け止める", "score": 7},
                {"choice_text": "あまり学んでいない", "score": 4},
                {"choice_text": "過去は振り返らない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの時間と、自分の時間をどのようにバランスさせますか？",
            "choices": [
                {"choice_text": "パートナーとの時間を最優先する", "score": 10},
                {"choice_text": "バランスを重視し、どちらも大切にする", "score": 7},
                {"choice_text": "自分の時間を優先する", "score": 4},
                {"choice_text": "あまり意識しない", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、相手にどこまで尽くせますか？",
            "choices": [
                {"choice_text": "全てを捧げる", "score": 10},
                {"choice_text": "できる範囲で尽くす", "score": 7},
                {"choice_text": "尽くすよりも尽くされたい", "score": 4},
                {"choice_text": "尽くすことはしない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーの意見に反対する場合、どう伝えますか？",
            "choices": [
                {"choice_text": "相手の気持ちを考慮しつつ、丁寧に自分の意見を伝える", "score": 10},
                {"choice_text": "遠回しに伝える", "score": 7},
                {"choice_text": "言わずに我慢する", "score": 4},
                {"choice_text": "感情的に反論する", "score": 1}
            ]
        },
        {
            "question_text": "恋愛における「依存」についてどう思いますか？",
            "choices": [
                {"choice_text": "お互いに支え合うのは良いが、過度な依存は避けるべき", "score": 10},
                {"choice_text": "ある程度の依存は愛情の証", "score": 7},
                {"choice_text": "依存されるのは苦手", "score": 4},
                {"choice_text": "依存は関係を壊す原因になる", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係を長続きさせる秘訣は何だと思いますか？",
            "choices": [
                {"choice_text": "コミュニケーションと感謝", "score": 10},
                {"choice_text": "共通の趣味や目標", "score": 7},
                {"choice_text": "適度な距離感", "score": 4},
                {"choice_text": "我慢と妥協", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、自分を偽ることはありますか？",
            "choices": [
                {"choice_text": "全くない。常に素の自分を見せる", "score": 10},
                {"choice_text": "相手に合わせて多少は演じる", "score": 7},
                {"choice_text": "よくある。本当の自分を見せるのが怖い", "score": 4},
                {"choice_text": "常に偽っている", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も幸せを感じる瞬間はどんな時ですか？",
            "choices": [
                {"choice_text": "一緒にいるだけで心が満たされる時", "score": 10},
                {"choice_text": "目標を達成し、喜びを分かち合う時", "score": 7},
                {"choice_text": "美味しい食事を一緒に食べている時", "score": 4},
                {"choice_text": "一人でゆっくり過ごしている時", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、年齢差は気になりますか？",
            "choices": [
                {"choice_text": "全く気にならない。愛があれば", "score": 10},
                {"choice_text": "多少は気になるが、問題ではない", "score": 7},
                {"choice_text": "気になる。同年代が良い", "score": 4},
                {"choice_text": "非常に気になる。年齢は重要", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの将来の夢を共有することは重要ですか？",
            "choices": [
                {"choice_text": "非常に重要。共に夢を追いかけたい", "score": 10},
                {"choice_text": "ある程度は重要。理解し合えればいい", "score": 7},
                {"choice_text": "あまり重要ではない。それぞれの夢でいい", "score": 4},
                {"choice_text": "全く重要ではない", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、最も苦手なタイプはどんな人ですか？",
            "choices": [
                {"choice_text": "嘘をつく人、不誠実な人", "score": 10},
                {"choice_text": "自己中心的でわがままな人", "score": 7},
                {"choice_text": "ネガティブで愚痴が多い人", "score": 4},
                {"choice_text": "束縛が激しい人", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も感謝していることは何ですか？",
            "choices": [
                {"choice_text": "どんな時も支え、理解してくれること", "score": 10},
                {"choice_text": "一緒に楽しい時間を過ごせること", "score": 7},
                {"choice_text": "自分の成長を促してくれること", "score": 4},
                {"choice_text": "そばにいてくれること", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、最も大切にしたいのは「与えること」と「受け取ること」どちらですか？",
            "choices": [
                {"choice_text": "与えること。相手の喜びが自分の喜び", "score": 10},
                {"choice_text": "どちらも同じくらい大切", "score": 7},
                {"choice_text": "受け取ること。愛されていると感じたい", "score": 4},
                {"choice_text": "あまり意識しない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、マンネリを感じた時どうしますか？",
            "choices": [
                {"choice_text": "新しいことに挑戦し、関係に刺激を与える", "score": 10},
                {"choice_text": "話し合い、改善策を考える", "score": 7},
                {"choice_text": "一人で気分転換をする", "score": 4},
                {"choice_text": "諦めてしまう", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、自分の意見を主張する方ですか？",
            "choices": [
                {"choice_text": "はい、積極的に主張します", "score": 10},
                {"choice_text": "状況に応じて主張します", "score": 7},
                {"choice_text": "あまり主張しません", "score": 4},
                {"choice_text": "いいえ、相手に合わせます", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの将来設計について、どの程度話し合いますか？",
            "choices": [
                {"choice_text": "具体的に、定期的に話し合う", "score": 10},
                {"choice_text": "漠然と話し合うことがある", "score": 7},
                {"choice_text": "あまり話し合わない", "score": 4},
                {"choice_text": "全く話し合わない", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、直感と論理、どちらを重視しますか？",
            "choices": [
                {"choice_text": "直感。フィーリングが大切", "score": 10},
                {"choice_text": "どちらも同じくらい大切", "score": 7},
                {"choice_text": "論理。冷静に判断したい", "score": 4},
                {"choice_text": "あまり意識しない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーの趣味や興味に、どこまで合わせられますか？",
            "choices": [
                {"choice_text": "積極的に合わせ、一緒に楽しむ", "score": 10},
                {"choice_text": "理解は示すが、無理には合わせない", "score": 7},
                {"choice_text": "あまり合わせられない", "score": 4},
                {"choice_text": "全く合わせられない", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、自分の時間を犠牲にできますか？",
            "choices": [
                {"choice_text": "はい、喜んで犠牲にします", "score": 10},
                {"choice_text": "ある程度は犠牲にできる", "score": 7},
                {"choice_text": "あまり犠牲にしたくない", "score": 4},
                {"choice_text": "いいえ、自分の時間が最優先", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最もストレスを感じる瞬間はどんな時ですか？",
            "choices": [
                {"choice_text": "意見が対立し、理解し合えない時", "score": 10},
                {"choice_text": "束縛や干渉を感じる時", "score": 7},
                {"choice_text": "相手が無関心な時", "score": 4},
                {"choice_text": "一人になりたい時", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、秘密を持つことはありますか？",
            "choices": [
                {"choice_text": "全くない。全てオープン", "score": 10},
                {"choice_text": "相手に言えない小さな秘密はある", "score": 7},
                {"choice_text": "いくつか秘密がある", "score": 4},
                {"choice_text": "秘密だらけ", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も改善したい点は何ですか？",
            "choices": [
                {"choice_text": "コミュニケーションの頻度と質", "score": 10},
                {"choice_text": "お互いの理解と尊重", "score": 7},
                {"choice_text": "一緒に過ごす時間", "score": 4},
                {"choice_text": "特にない", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、相手に求めるのは「刺激」と「安定」どちらですか？",
            "choices": [
                {"choice_text": "刺激。常に新鮮な関係でいたい", "score": 10},
                {"choice_text": "どちらもバランス良く", "score": 7},
                {"choice_text": "安定。穏やかな関係を築きたい", "score": 4},
                {"choice_text": "あまり意識しない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も自信がある点は何ですか？",
            "choices": [
                {"choice_text": "相手を深く愛し、支えることができる", "score": 10},
                {"choice_text": "どんな困難も共に乗り越えられる", "score": 7},
                {"choice_text": "相手を笑顔にできる", "score": 4},
                {"choice_text": "特にない", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、自分の魅力をどのようにアピールしますか？",
            "choices": [
                {"choice_text": "積極的に自分を表現し、アピールする", "score": 10},
                {"choice_text": "自然体でいることで、魅力を伝える", "score": 7},
                {"choice_text": "あまりアピールしない", "score": 4},
                {"choice_text": "どうアピールすればいいか分からない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も避けたい話題は何ですか？",
            "choices": [
                {"choice_text": "過去の恋愛話", "score": 10},
                {"choice_text": "金銭問題", "score": 7},
                {"choice_text": "将来の計画", "score": 4},
                {"choice_text": "特にない", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、相手に求めるのは「共感」と「アドバイス」どちらですか？",
            "choices": [
                {"choice_text": "共感。ただ話を聞いてほしい", "score": 10},
                {"choice_text": "どちらも同じくらい大切", "score": 7},
                {"choice_text": "アドバイス。具体的な解決策がほしい", "score": 4},
                {"choice_text": "あまり意識しない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も感謝していることは何ですか？",
            "choices": [
                {"choice_text": "どんな時も支え、理解してくれること", "score": 10},
                {"choice_text": "一緒に楽しい時間を過ごせること", "score": 7},
                {"choice_text": "自分の成長を促してくれること", "score": 4},
                {"choice_text": "そばにいてくれること", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、相手に求めるのは「外見」と「内面」どちらですか？",
            "choices": [
                {"choice_text": "内面。性格や価値観が重要", "score": 10},
                {"choice_text": "どちらも同じくらい大切", "score": 7},
                {"choice_text": "外見。第一印象が重要", "score": 4},
                {"choice_text": "あまり意識しない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も許せない行動は何ですか？",
            "choices": [
                {"choice_text": "嘘をつくこと、裏切ること", "score": 10},
                {"choice_text": "約束を破ること", "score": 7},
                {"choice_text": "連絡を無視すること", "score": 4},
                {"choice_text": "無関心な態度をとること", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、自分の感情をコントロールできますか？",
            "choices": [
                {"choice_text": "はい、常に冷静でいられます", "score": 10},
                {"choice_text": "ある程度はできますが、感情的になることも", "score": 7},
                {"choice_text": "あまりできません。感情的になりやすい", "score": 4},
                {"choice_text": "全くできません。感情に流されやすい", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も大切にしたい「時間」はどんな時ですか？",
            "choices": [
                {"choice_text": "二人きりで過ごすロマンチックな時間", "score": 10},
                {"choice_text": "一緒に趣味を楽しむ時間", "score": 7},
                {"choice_text": "友人も交えて賑やかに過ごす時間", "score": 4},
                {"choice_text": "それぞれの時間を尊重する", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、相手に求めるのは「癒し」と「刺激」どちらですか？",
            "choices": [
                {"choice_text": "癒し。安らぎを与えてくれる存在", "score": 10},
                {"choice_text": "どちらも同じくらい大切", "score": 7},
                {"choice_text": "刺激。常に新しい発見がほしい", "score": 4},
                {"choice_text": "あまり意識しない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も譲れないことは何ですか？",
            "choices": [
                {"choice_text": "信頼と誠実さ", "score": 10},
                {"choice_text": "自由と自立", "score": 7},
                {"choice_text": "金銭感覚の一致", "score": 4},
                {"choice_text": "外見の魅力", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、自分の意見を曲げることはできますか？",
            "choices": [
                {"choice_text": "はい、相手のためならできます", "score": 10},
                {"choice_text": "状況による。納得できれば", "score": 7},
                {"choice_text": "あまりできません", "score": 4},
                {"choice_text": "いいえ、自分の意見は曲げない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も大切にしたい「言葉」は何ですか？",
            "choices": [
                {"choice_text": "「愛してる」", "score": 10},
                {"choice_text": "「ありがとう」", "score": 7},
                {"choice_text": "「ごめんね」", "score": 4},
                {"choice_text": "「大丈夫」", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、相手に求めるのは「リード」と「対等」どちらですか？",
            "choices": [
                {"choice_text": "リードしてほしい", "score": 10},
                {"choice_text": "対等な関係が良い", "score": 7},
                {"choice_text": "どちらでもいい", "score": 4},
                {"choice_text": "あまり意識しない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も苦手なことは何ですか？",
            "choices": [
                {"choice_text": "束縛されること", "score": 10},
                {"choice_text": "意見の押し付け", "score": 7},
                {"choice_text": "無関心な態度", "score": 4},
                {"choice_text": "喧嘩", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、自分の気持ちを隠すことはありますか？",
            "choices": [
                {"choice_text": "全くない。常にオープン", "score": 10},
                {"choice_text": "相手を気遣って隠すことがある", "score": 7},
                {"choice_text": "よくある。本音を言えない", "score": 4},
                {"choice_text": "常に隠している", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も大切にしたい「行動」は何ですか？",
            "choices": [
                {"choice_text": "ハグやキスなどのスキンシップ", "score": 10},
                {"choice_text": "一緒に食事をする", "score": 7},
                {"choice_text": "手をつないで歩く", "score": 4},
                {"choice_text": "特にない", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、相手に求めるのは「理解」と「共感」どちらですか？",
            "choices": [
                {"choice_text": "理解。深く分かり合いたい", "score": 10},
                {"choice_text": "どちらも同じくらい大切", "score": 7},
                {"choice_text": "共感。気持ちを分かってほしい", "score": 4},
                {"choice_text": "あまり意識しない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も大切にしたい「記念日」は何ですか？",
            "choices": [
                {"choice_text": "二人の出会った日", "score": 10},
                {"choice_text": "付き合った日", "score": 7},
                {"choice_text": "誕生日", "score": 4},
                {"choice_text": "特にない", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、自分の魅力を高めるために努力しますか？",
            "choices": [
                {"choice_text": "はい、常に努力しています", "score": 10},
                {"choice_text": "ある程度は努力します", "score": 7},
                {"choice_text": "あまり努力しません", "score": 4},
                {"choice_text": "全く努力しません", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も避けたい「感情」は何ですか？",
            "choices": [
                {"choice_text": "嫉妬", "score": 10},
                {"choice_text": "不安", "score": 7},
                {"choice_text": "不満", "score": 4},
                {"choice_text": "無関心", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、相手に求めるのは「言葉」と「行動」どちらですか？",
            "choices": [
                {"choice_text": "行動。言葉よりも行動で示してほしい", "score": 10},
                {"choice_text": "どちらも同じくらい大切", "score": 7},
                {"choice_text": "言葉。気持ちを伝えてほしい", "score": 4},
                {"choice_text": "あまり意識しない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も大切にしたい「約束」は何ですか？",
            "choices": [
                {"choice_text": "どんな時も正直でいること", "score": 10},
                {"choice_text": "お互いを尊重すること", "score": 7},
                {"choice_text": "秘密を持たないこと", "score": 4},
                {"choice_text": "毎日連絡を取ること", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、自分の価値観を曲げることはできますか？",
            "choices": [
                {"choice_text": "はい、相手のためならできます", "score": 10},
                {"choice_text": "状況による。納得できれば", "score": 7},
                {"choice_text": "あまりできません", "score": 4},
                {"choice_text": "いいえ、自分の価値観は曲げない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も大切にしたい「場所」はどこですか？",
            "choices": [
                {"choice_text": "二人の思い出の場所", "score": 10},
                {"choice_text": "お互いの家", "score": 7},
                {"choice_text": "カフェやレストラン", "score": 4},
                {"choice_text": "特にない", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、相手に求めるのは「共通点」と「相違点」どちらですか？",
            "choices": [
                {"choice_text": "共通点。分かり合えることが大切", "score": 10},
                {"choice_text": "どちらも同じくらい大切", "score": 7},
                {"choice_text": "相違点。新しい発見がほしい", "score": 4},
                {"choice_text": "あまり意識しない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も苦手な「会話」は何ですか？",
            "choices": [
                {"choice_text": "将来の計画に関する真剣な話", "score": 10},
                {"choice_text": "自分の意見を主張する議論", "score": 7},
                {"choice_text": "相手の不満を聞くこと", "score": 4},
                {"choice_text": "特にない", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、自分のペースを大切にしますか？",
            "choices": [
                {"choice_text": "はい、自分のペースを崩したくない", "score": 10},
                {"choice_text": "ある程度は大切にするが、相手に合わせることも", "score": 7},
                {"choice_text": "あまり意識しない", "score": 4},
                {"choice_text": "いいえ、相手のペースに合わせる", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も大切にしたい「感情」は何ですか？",
            "choices": [
                {"choice_text": "幸福感", "score": 10},
                {"choice_text": "安心感", "score": 7},
                {"choice_text": "充実感", "score": 4},
                {"choice_text": "自由", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、相手に求めるのは「精神的な繋がり」と「肉体的な繋がり」どちらですか？",
            "choices": [
                {"choice_text": "精神的な繋がり。心が通じ合うことが大切", "score": 10},
                {"choice_text": "どちらも同じくらい大切", "score": 7},
                {"choice_text": "肉体的な繋がり。触れ合うことが大切", "score": 4},
                {"choice_text": "あまり意識しない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も苦手な「状況」は何ですか？",
            "choices": [
                {"choice_text": "喧嘩や口論", "score": 10},
                {"choice_text": "すれ違いや誤解", "score": 7},
                {"choice_text": "マンネリ化", "score": 4},
                {"choice_text": "束縛されること", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、自分の直感を信じますか？",
            "choices": [
                {"choice_text": "はい、常に信じます", "score": 10},
                {"choice_text": "ある程度は信じるが、最終的には論理的に考える", "score": 7},
                {"choice_text": "いいえ、直感よりも現実的な判断を重視する", "score": 4},
                {"choice_text": "全く信じない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も大切にしたい「価値観」は何ですか？",
            "choices": [
                {"choice_text": "誠実さ", "score": 10},
                {"choice_text": "優しさ", "score": 7},
                {"choice_text": "自立心", "score": 4},
                {"choice_text": "経済力", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、相手に求めるのは「共通の趣味」と「新しい発見」どちらですか？",
            "choices": [
                {"choice_text": "共通の趣味。一緒に楽しめることが大切", "score": 10},
                {"choice_text": "どちらも同じくらい大切", "score": 7},
                {"choice_text": "新しい発見。刺激がほしい", "score": 4},
                {"choice_text": "あまり意識しない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も苦手な「タイプ」は何ですか？",
            "choices": [
                {"choice_text": "嘘つきな人", "score": 10},
                {"choice_text": "自己中心的な人", "score": 7},
                {"choice_text": "ネガティブな人", "score": 4},
                {"choice_text": "束縛する人", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、自分の感情を素直に表現できますか？",
            "choices": [
                {"choice_text": "はい、素直に表現できます", "score": 10},
                {"choice_text": "ある程度はできますが、躊躇することも", "score": 7},
                {"choice_text": "あまりできません。感情を隠しがち", "score": 4},
                {"choice_text": "全くできません。感情を抑え込んでしまう", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も大切にしたい「思い出」は何ですか？",
            "choices": [
                {"choice_text": "初めて出会った日のこと", "score": 10},
                {"choice_text": "一緒に旅行に行った時のこと", "score": 7},
                {"choice_text": "何気ない日常の出来事", "score": 4},
                {"choice_text": "特にない", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、相手に求めるのは「共依存」と「自立」どちらですか？",
            "choices": [
                {"choice_text": "自立。お互いが自立した関係が良い", "score": 10},
                {"choice_text": "どちらもバランス良く", "score": 7},
                {"choice_text": "共依存。常に一緒にいたい", "score": 4},
                {"choice_text": "あまり意識しない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も苦手な「状況」は何ですか？",
            "choices": [
                {"choice_text": "喧嘩や口論", "score": 10},
                {"choice_text": "すれ違いや誤解", "score": 7},
                {"choice_text": "マンネリ化", "score": 4},
                {"choice_text": "束縛されること", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、自分の気持ちを伝えるのは得意ですか？",
            "choices": [
                {"choice_text": "はい、得意です", "score": 10},
                {"choice_text": "ある程度は得意ですが、苦手な時も", "score": 7},
                {"choice_text": "あまり得意ではありません", "score": 4},
                {"choice_text": "いいえ、苦手です", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も大切にしたい「言葉」は何ですか？",
            "choices": [
                {"choice_text": "「愛してる」", "score": 10},
                {"choice_text": "「ありがとう」", "score": 7},
                {"choice_text": "「ごめんね」", "score": 4},
                {"choice_text": "「大丈夫」", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、相手に求めるのは「刺激」と「安定」どちらですか？",
            "choices": [
                {"choice_text": "刺激。常に新鮮な関係でいたい", "score": 10},
                {"choice_text": "どちらもバランス良く", "score": 7},
                {"choice_text": "安定。穏やかな関係を築きたい", "score": 4},
                {"choice_text": "あまり意識しない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も自信がある点は何ですか？",
            "choices": [
                {"choice_text": "相手を深く愛し、支えることができる", "score": 10},
                {"choice_text": "どんな困難も共に乗り越えられる", "score": 7},
                {"choice_text": "相手を笑顔にできる", "score": 4},
                {"choice_text": "特にない", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、自分の魅力をどのようにアピールしますか？",
            "choices": [
                {"choice_text": "積極的に自分を表現し、アピールする", "score": 10},
                {"choice_text": "自然体でいることで、魅力を伝える", "score": 7},
                {"choice_text": "あまりアピールしない", "score": 4},
                {"choice_text": "どうアピールすればいいか分からない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も避けたい話題は何ですか？",
            "choices": [
                {"choice_text": "過去の恋愛話", "score": 10},
                {"choice_text": "金銭問題", "score": 7},
                {"choice_text": "将来の計画", "score": 4},
                {"choice_text": "特にない", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、相手に求めるのは「共感」と「アドバイス」どちらですか？",
            "choices": [
                {"choice_text": "共感。ただ話を聞いてほしい", "score": 10},
                {"choice_text": "どちらも同じくらい大切", "score": 7},
                {"choice_text": "アドバイス。具体的な解決策がほしい", "score": 4},
                {"choice_text": "あまり意識しない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も感謝していることは何ですか？",
            "choices": [
                {"choice_text": "どんな時も支え、理解してくれること", "score": 10},
                {"choice_text": "一緒に楽しい時間を過ごせること", "score": 7},
                {"choice_text": "自分の成長を促してくれること", "score": 4},
                {"choice_text": "そばにいてくれること", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、相手に求めるのは「外見」と「内面」どちらですか？",
            "choices": [
                {"choice_text": "内面。性格や価値観が重要", "score": 10},
                {"choice_text": "どちらも同じくらい大切", "score": 7},
                {"choice_text": "外見。第一印象が重要", "score": 4},
                {"choice_text": "あまり意識しない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も許せない行動は何ですか？",
            "choices": [
                {"choice_text": "嘘をつくこと、裏切ること", "score": 10},
                {"choice_text": "約束を破ること", "score": 7},
                {"choice_text": "連絡を無視すること", "score": 4},
                {"choice_text": "無関心な態度をとること", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、自分の感情をコントロールできますか？",
            "choices": [
                {"choice_text": "はい、常に冷静でいられます", "score": 10},
                {"choice_text": "ある程度はできますが、感情的になることも", "score": 7},
                {"choice_text": "あまりできません。感情的になりやすい", "score": 4},
                {"choice_text": "全くできません。感情に流されやすい", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も大切にしたい「時間」はどんな時ですか？",
            "choices": [
                {"choice_text": "二人きりで過ごすロマンチックな時間", "score": 10},
                {"choice_text": "一緒に趣味を楽しむ時間", "score": 7},
                {"choice_text": "友人も交えて賑やかに過ごす時間", "score": 4},
                {"choice_text": "それぞれの時間を尊重する", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、相手に求めるのは「癒し」と「刺激」どちらですか？",
            "choices": [
                {"choice_text": "癒し。安らぎを与えてくれる存在", "score": 10},
                {"choice_text": "どちらも同じくらい大切", "score": 7},
                {"choice_text": "刺激。常に新しい発見がほしい", "score": 4},
                {"choice_text": "あまり意識しない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も譲れないことは何ですか？",
            "choices": [
                {"choice_text": "信頼と誠実さ", "score": 10},
                {"choice_text": "自由と自立", "score": 7},
                {"choice_text": "金銭感覚の一致", "score": 4},
                {"choice_text": "外見の魅力", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、自分の意見を曲げることはできますか？",
            "choices": [
                {"choice_text": "はい、相手のためならできます", "score": 10},
                {"choice_text": "状況による。納得できれば", "score": 7},
                {"choice_text": "あまりできません", "score": 4},
                {"choice_text": "いいえ、自分の意見は曲げない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も大切にしたい「言葉」は何ですか？",
            "choices": [
                {"choice_text": "「愛してる」", "score": 10},
                {"choice_text": "「ありがとう」", "score": 7},
                {"choice_text": "「ごめんね」", "score": 4},
                {"choice_text": "「大丈夫」", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、相手に求めるのは「リード」と「対等」どちらですか？",
            "choices": [
                {"choice_text": "リードしてほしい", "score": 10},
                {"choice_text": "対等な関係が良い", "score": 7},
                {"choice_text": "どちらでもいい", "score": 4},
                {"choice_text": "あまり意識しない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も苦手なことは何ですか？",
            "choices": [
                {"choice_text": "束縛されること", "score": 10},
                {"choice_text": "意見の押し付け", "score": 7},
                {"choice_text": "無関心な態度", "score": 4},
                {"choice_text": "喧嘩", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、自分の気持ちを隠すことはありますか？",
            "choices": [
                {"choice_text": "全くない。常にオープン", "score": 10},
                {"choice_text": "相手を気遣って隠すことがある", "score": 7},
                {"choice_text": "よくある。本音を言えない", "score": 4},
                {"choice_text": "常に隠している", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も大切にしたい「行動」は何ですか？",
            "choices": [
                {"choice_text": "ハグやキスなどのスキンシップ", "score": 10},
                {"choice_text": "一緒に食事をする", "score": 7},
                {"choice_text": "手をつないで歩く", "score": 4},
                {"choice_text": "特にない", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、相手に求めるのは「理解」と「共感」どちらですか？",
            "choices": [
                {"choice_text": "理解。深く分かり合いたい", "score": 10},
                {"choice_text": "どちらも同じくらい大切", "score": 7},
                {"choice_text": "共感。気持ちを分かってほしい", "score": 4},
                {"choice_text": "あまり意識しない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も大切にしたい「記念日」は何ですか？",
            "choices": [
                {"choice_text": "二人の出会った日", "score": 10},
                {"choice_text": "付き合った日", "score": 7},
                {"choice_text": "誕生日", "score": 4},
                {"choice_text": "特にない", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、自分の魅力を高めるために努力しますか？",
            "choices": [
                {"choice_text": "はい、常に努力しています", "score": 10},
                {"choice_text": "ある程度は努力します", "score": 7},
                {"choice_text": "あまり努力しません", "score": 4},
                {"choice_text": "全く努力しません", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も避けたい「感情」は何ですか？",
            "choices": [
                {"choice_text": "嫉妬", "score": 10},
                {"choice_text": "不安", "score": 7},
                {"choice_text": "不満", "score": 4},
                {"choice_text": "無関心", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、相手に求めるのは「言葉」と「行動」どちらですか？",
            "choices": [
                {"choice_text": "行動。言葉よりも行動で示してほしい", "score": 10},
                {"choice_text": "どちらも同じくらい大切", "score": 7},
                {"choice_text": "言葉。気持ちを伝えてほしい", "score": 4},
                {"choice_text": "あまり意識しない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も大切にしたい「約束」は何ですか？",
            "choices": [
                {"choice_text": "どんな時も正直でいること", "score": 10},
                {"choice_text": "お互いを尊重すること", "score": 7},
                {"choice_text": "秘密を持たないこと", "score": 4},
                {"choice_text": "毎日連絡を取ること", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、自分の価値観を曲げることはできますか？",
            "choices": [
                {"choice_text": "はい、相手のためならできます", "score": 10},
                {"choice_text": "状況による。納得できれば", "score": 7},
                {"choice_text": "あまりできません", "score": 4},
                {"choice_text": "いいえ、自分の価値観は曲げない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も大切にしたい「場所」はどこですか？",
            "choices": [
                {"choice_text": "二人の思い出の場所", "score": 10},
                {"choice_text": "お互いの家", "score": 7},
                {"choice_text": "カフェやレストラン", "score": 4},
                {"choice_text": "特にない", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、相手に求めるのは「共通点」と「相違点」どちらですか？",
            "choices": [
                {"choice_text": "共通点。分かり合えることが大切", "score": 10},
                {"choice_text": "どちらも同じくらい大切", "score": 7},
                {"choice_text": "相違点。新しい発見がほしい", "score": 4},
                {"choice_text": "あまり意識しない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も苦手な「会話」は何ですか？",
            "choices": [
                {"choice_text": "将来の計画に関する真剣な話", "score": 10},
                {"choice_text": "自分の意見を主張する議論", "score": 7},
                {"choice_text": "相手の不満を聞くこと", "score": 4},
                {"choice_text": "特にない", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、自分のペースを大切にしますか？",
            "choices": [
                {"choice_text": "はい、自分のペースを崩したくない", "score": 10},
                {"choice_text": "ある程度は大切にするが、相手に合わせることも", "score": 7},
                {"choice_text": "あまり意識しない", "score": 4},
                {"choice_text": "いいえ、相手のペースに合わせる", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も大切にしたい「感情」は何ですか？",
            "choices": [
                {"choice_text": "幸福感", "score": 10},
                {"choice_text": "安心感", "score": 7},
                {"choice_text": "充実感", "score": 4},
                {"choice_text": "自由", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、相手に求めるのは「精神的な繋がり」と「肉体的な繋がり」どちらですか？",
            "choices": [
                {"choice_text": "精神的な繋がり。心が通じ合うことが大切", "score": 10},
                {"choice_text": "どちらも同じくらい大切", "score": 7},
                {"choice_text": "肉体的な繋がり。触れ合うことが大切", "score": 4},
                {"choice_text": "あまり意識しない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も苦手な「状況」は何ですか？",
            "choices": [
                {"choice_text": "喧嘩や口論", "score": 10},
                {"choice_text": "すれ違いや誤解", "score": 7},
                {"choice_text": "マンネリ化", "score": 4},
                {"choice_text": "束縛されること", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、自分の直感を信じますか？",
            "choices": [
                {"choice_text": "はい、常に信じます", "score": 10},
                {"choice_text": "ある程度は信じるが、最終的には論理的に考える", "score": 7},
                {"choice_text": "いいえ、直感よりも現実的な判断を重視する", "score": 4},
                {"choice_text": "全く信じない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も大切にしたい「価値観」は何ですか？",
            "choices": [
                {"choice_text": "誠実さ", "score": 10},
                {"choice_text": "優しさ", "score": 7},
                {"choice_text": "自立心", "score": 4},
                {"choice_text": "経済力", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、相手に求めるのは「共通の趣味」と「新しい発見」どちらですか？",
            "choices": [
                {"choice_text": "共通の趣味。一緒に楽しめることが大切", "score": 10},
                {"choice_text": "どちらも同じくらい大切", "score": 7},
                {"choice_text": "新しい発見。刺激がほしい", "score": 4},
                {"choice_text": "あまり意識しない", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も苦手な「タイプ」は何ですか？",
            "choices": [
                {"choice_text": "嘘つきな人", "score": 10},
                {"choice_text": "自己中心的な人", "score": 7},
                {"choice_text": "ネガティブな人", "score": 4},
                {"choice_text": "束縛する人", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、自分の感情を素直に表現できますか？",
            "choices": [
                {"choice_text": "はい、素直に表現できます", "score": 10},
                {"choice_text": "ある程度はできますが、躊躇することも", "score": 7},
                {"choice_text": "あまりできません。感情を隠しがち", "score": 4},
                {"choice_text": "全くできません。感情を抑え込んでしまう", "score": 1}
            ]
        },
        {
            "question_text": "パートナーとの関係で、最も大切にしたい「思い出」は何ですか？",
            "choices": [
                {"choice_text": "初めて出会った日のこと", "score": 10},
                {"choice_text": "一緒に旅行に行った時のこと", "score": 7},
                {"choice_text": "何気ない日常の出来事", "score": 4},
                {"choice_text": "特にない", "score": 1}
            ]
        },
        {
            "question_text": "恋愛において、相手に求めるのは「共依存」と「自立」どちらですか？",
            "choices": [
                {"choice_text": "自立。お互いが自立した関係が良い", "score": 10},
                {"choice_text": "どちらもバランス良く", "score": 7},
                {"choice_text": "共依存。常に一緒にいたい", "score": 4},
                {"choice_text": "あまり意識しない", "score": 1}
            ]
        }
    ]

    # 50個の質問をランダムに選択してIDを付与
    random_questions = random.sample(questions_data, 50)
    for i, q in enumerate(random_questions):
        q["id"] = i + 1
    return random_questions

questions = generate_question_and_choices(50)

with open("questions.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("questions.json generated successfully.")


