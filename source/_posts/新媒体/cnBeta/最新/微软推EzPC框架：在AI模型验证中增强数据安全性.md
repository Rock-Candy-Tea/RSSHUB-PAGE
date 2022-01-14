
---
title: '微软推EzPC框架：在AI模型验证中增强数据安全性'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0114/68e79fcb0d90e4f.webp'
author: cnBeta
comments: false
date: Fri, 14 Jan 2022 07:38:22 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0114/68e79fcb0d90e4f.webp'
---

<div>   
在数据科学领域工作过的人都知道，开发一个人工智能模型通常可以概括为 3 个阶段：训练、验证和测试。在测试模型的准确性时，选择验证集来调整超参数（hyperparameters）时，通常有很多考虑。<br>
 <p>为了进行准确的模型评估，企业倾向于使用一部分真实数据进行验证，但自然会有很多安全和隐私方面的考虑，特别是在处理个人身份信息（PII）方面。</p><p>如果你的模型是由一个外部公司开发的，你基本上有两个选择。要么该公司与你分享其模型，这将对其知识产权保护构成风险；要么你与他们分享你的真实数据，这对你来说是一种隐私风险，也可能导致模型对真实数据过度拟合。在做出这两种困难的选择时，也有很多法律障碍需要跳过。因此，虽然企业希望尽快采用人工智能，但在处理数据时，模型开发过程无论是内部还是外部，他们都面临着挑战。</p><p><img src="https://static.cnbetacdn.com/article/2022/0114/68e79fcb0d90e4f.webp" alt="ezgif.com-gif-maker.webp" referrerpolicy="no-referrer"></p><p><strong>为了解决这个问题，<a href="https://www.microsoft.com/en-us/research/blog/ezpc-increased-data-security-in-the-ai-model-validation-process/" target="_blank">微软正在研究一个名为 EzPC 的新框架</a>，它代表着“轻松安全的多方计算”。</strong>从本质上讲，EzPC 是基于安全的多方计算（MPC）的。MPC 使多方能够使用加密技术联合计算一个函数，而不向对方透露他们的数据。</p><p>虽然 MPC 已经存在多年，但事实证明它很难实现，因为在计算多个函数时，使其具有可扩展性和高效性的挑战。EzPC 通过使用 MPC 作为构建块来解决这些问题，并使开发者--不仅仅是密码学专家--能够在此基础上进行扩展。</p><p><img src="https://static.cnbetacdn.com/article/2022/0114/3010c8f81554063.webp" alt="hkxv456m.webp" referrerpolicy="no-referrer"></p><p>微软表示</p><blockquote><p><strong>EzPC 的核心是两项创新。</strong></p><p><strong>● CrypTFlow 模块化编译器</strong></p><p>将用于 ML 推理的 TensorFlow 或 Open Neural Network Exchange（ONNX）代码作为输入，并自动生成类似 C 的代码，然后可以将其编译为各种 MPC 协议。这个编译器既是“MPC感知”的，也是优化的，确保了 MPC 协议的高效和可扩展。</p><p>●<strong> 高性能的加密协议</strong></p><p>第二个创新是一套高性能的加密协议，用于安全地计算复杂的ML函数。</p></blockquote><p>微软吹嘘说，EzPC 在与斯坦福大学研究人员的测试中实现了“有史以来第一次对生产级人工智能模型的安全验证”，从而证明你不需要分享数据来进行验证。尽管微软的EzPC模型在“两个标准的云端虚拟机”上用了15分钟做带有验证元素的安全推理--这比普通推理要长 3000 倍，但该公司表示，这并不重要，因为计算并行可以解决这个问题。</p><p>根据目前的方法，验证集中的 500 多个图像在五天的时间内完成了推理，总成本不到 100 美元。微软声称，如果所有的数据都是并行运行的，它可以在 15 分钟内完成对整个集合的推理。你可以在这里发表的论文中探讨这些发现。</p>   
</div>
            