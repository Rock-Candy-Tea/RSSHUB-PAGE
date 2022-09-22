
---
title: 'OpenAI宣布开源多语言语音识别系统Whisper'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0920/806305ff22d8566.jpg'
author: cnBeta
comments: false
date: Thu, 22 Sep 2022 06:41:08 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0920/806305ff22d8566.jpg'
---

<div>   
尽管包括 Google、亚马逊和 Meta 在内的科技巨头，都将各自开发的功能强大的语音识别系统置于其软件和服务的核心地位。但在人工智能和机器学习领域，语音识别仍是一个颇具挑战性的话题。<strong>好消息是，今日 OpenAI 隆重地宣布了 Whisper 的开源 —— 可知作为一套自动语音识别系统，官方宣称它能够实现多种语言的强大转录、并将它们翻译成英语。</strong><br>
<p><img src="https://static.cnbetacdn.com/article/2022/0920/806305ff22d8566.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：OpenAI <a href="https://openai.com/blog/whisper/" target="_self">Blog</a>）</p><p>OpenAI 表示，Whisper 的不同之处，在于其接受了从网络收集的 68 万小时的多语言和“多任务”训练数据，从而提升了该方案对独特口音、背景噪声和技术术语的识别能力。</p><p><strong>官方 <a href="https://github.com/openai/whisper/blob/main/model-card.md" target="_self">GitHub</a> 存储库上的概述称：</strong></p><blockquote><p>Whisper 模型的主要目标用户，是研究当前模型稳健性、泛化、能力、偏差和约束的 AI 研究人员。</p><p>与此同时，它也很适合作为面向开发者的自动语音识别解决方案尤其是英语语音识别。</p><p>感兴趣的朋友，可以从托管平台上下载 Whisper 系统的多个版本，其模型在大约 10 种语言上展现出了强大的 ASR 结果。</p><p>此外假如在某些任务上加以微调的话，它们还有望在语音活动检测、讲述者分类等应用场景下表现出额外的能力。</p></blockquote><p><a href="https://static.cnbetacdn.com/article/2022/0922/b18a1a7d121e3a9.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0922/b18a1a7d121e3a9.png" alt="1.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">架构示意</p><p>遗憾的是，Whisper 尚未在相关领域得到强有力的评估、且模型也有其局限性 —— 有其在文本预测领域。</p><p>由于该系统接受了大量“嘈杂”的数据训练，OpenAI 决定提前给大家打一剂预防针，警告称 Whisper 可能在转录中包含实际上未讲述的单词。</p><p>原因可能是 Whisper 既试图预测音频中的下一个单词、又试图转录音频本身。</p><p><a href="https://static.cnbetacdn.com/article/2022/0922/99090a8b620c7d0.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0922/99090a8b620c7d0.png" alt="2.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">流程示例</p><p>此外 Whisper 在不同语言场景下的表现也不大一致，尤其涉及在训练数据中没有很好被代表的语言的讲述者时，其错误率也会更高。</p><p>不过后者在语音识别领域早已不是什么新鲜事，即使业内首屈一指的系统，也一直受到此类偏差的困扰。</p><p>参考斯坦福大学在 2020 年分享的一项研究结果 —— 相较于黑人，来自亚马逊、<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>、Google、IBM 和<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>的系统，针对白人用户的错误率要低得多（大约 35%）。</p><p><a href="https://static.cnbetacdn.com/article/2022/0922/d034ef407798ec6.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0922/d034ef407798ec6.png" alt="3.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">Whisper 有约 1/3 的音频数据集为非英语</p><p>即便如此，OpenAI 还是认为 Whisper 的转录功能，可被用于改进现有的可访问性工具。其在 GitHub 上写道：</p><blockquote><p>尽管 Whisper 模型不适用于开箱即用的实时转录，但其速度和大小表明，其他人可在此基础上构建近乎实时的语音识别和翻译应用程序。</p><p>建立在 Whisper 模型之上的有益应用程序，其价值切实地表明了这些模型的不同性能，有望发挥出真正的经济影响力。</p><p>我们希望大家能够将该技术积极应用于有益目的，使自动语音识别技术更易获得改进、让更多参与者能够打造出更负责任的项目。</p><p>在速度和准确性的双重优势下，Whisper 将允许对大量通信提供可负担得起的自动转录和翻译体验。</p></blockquote><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1255467.htm" target="_blank">[视频]OpenAI展示DALL-E 2：AI图像生成器支持编辑图像了</a></p><p><a href="https://www.cnbeta.com/articles/tech/1311077.htm" target="_blank">OpenAI的DALL-E绘画AI 已能够扩展创作更大的图像</a></p><p><a href="https://www.cnbeta.com/articles/tech/1318393.htm" target="_blank">过滤系统升级：OpenAI再次开放DALL-E 2的面容编辑功能</a></p></div>   
</div>
            