
---
title: 'NLP 常规任务用 bert 类模型几行代码就能解决，那 NLP 岗主要存在的价值是什么？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://picsum.photos/400/300?random=417'
author: 知乎
comments: false
date: Wed, 27 Oct 2021 13:28:19 GMT
thumbnail: 'https://picsum.photos/400/300?random=417'
---

<div>   
夕小瑶的回答<br><br><p>NLP常规任务几行代码就能解决？</p><p>什么叫常规任务呢，文本分类？文本匹配？</p><p>好，那题主可以试试训练一个文本匹配模型，在训练集完全没见过以下样本的情况下，打出正确的匹配标签</p><ol><li>text_a："马思纯太美了，美哭了"，text_b：“马思纯哭了，太美了”，label：0</li><li>text_a："马思纯太美了，我哭了"，text_b：“马思纯美哭我了”，label：1</li><li>text_a："北京到上海有哪些航班"，text_b：“上海到北京有哪些航班”，label：0</li><li>text_a："北京到上海有多远"，text_b：“上海到北京有多远”，label：1</li><li>text_a："三年级有哪些教学科目"，text_b：“四年级有哪些教学科目”，label：0</li><li>text_a："20岁女生好用的水乳"，text_b：“21岁女生好用的水乳”，label：1</li><li>text_a："20岁女生好用的精华"，text_b：“30岁女生好用的精华”，label：0</li><li>text_a："苹果5s怎么拆机"，text_b：“苹果6s怎么拆机”，label：0</li><li>text_a："张柏芝的孩子是谁"，text_b：“张柏芝的孩子是谁的”，label：0</li></ol><p>开源文本匹配数据集你随便用，如果你几行代码训出来的模型能做对以上9个case，请联系我（溜了溜了</p><p><br></p><p>——————</p><p>做点补充，以上case中有一半是真实搜索中遇到的hardcase，剩下的人为补充的是为了test模型能力而构造的对抗样本。借这9个case是想说明，文本分类/文本匹配这种任务可以简单到不需要用模型就100% acc，也可以困难到一个任务让一个上万人的公司做了这么多年都挨骂。</p><p>不是只有建模起来复杂的任务才叫难任务，建模容易做起来难的任务在真实的搜索场景中比比皆是。在开放域搜索业务中做nlp，大概你也会每天跟我一样念叨nlp is hard吧m(_ _)m</p>  
</div>
            