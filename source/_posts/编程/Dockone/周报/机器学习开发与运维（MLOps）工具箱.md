
---
title: '机器学习开发与运维（MLOps）工具箱'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210816/754d8cbd0d62068d899c64cbc392d41c.jpg'
author: Dockone
comments: false
date: 2021-08-18 09:08:02
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210816/754d8cbd0d62068d899c64cbc392d41c.jpg'
---

<div>   
<br>与通用应用程序编程相比，机器学习（Machine Learning）是一个相对较新的工作领域。如今，硬件和软件均已支持大型机器学习项目，以使公司能够更好地进行决策，而机器学习的工具和解决方案已席卷了技术领域。这产生了一个称为MLOps的新领域。MLOps把来自DevOps的实践协作，版本控制，自动化测试，合规性，安全性和CI/CD应用于机器学习领域。  <br>
<br>本文将回顾进行机器学习开发所需的主要工具和技术，重点关注MLOps以及如何应用MLOps有效地建立机器学习模型。<br>
<h3>机器学习周期</h3>尽管MLOps这个概念还没有存在很长时间了，但是由于机器学习周期的复杂性，MLOps的技术前景是非常广阔的。在本文中，我们将讨论机器学习开发中的以下主题：<br>
<ol><li><br>数据和特征管理<br>
<ul><li>数据储存</li><li>数据准备</li><li>数据探索</li><li>特征储存</li></ul></li><li><br>模型开发<br>
<ul><li>模型注册</li><li>模型训练与验证</li><li>版本控制</li></ul></li><li><br>模型运作<br>
<ul><li>自动化测试</li><li>持续化的集成，部署和培训（CI / CD / CT）</li><li>模型服务基础架构</li></ul></li><li><br>监控<br>
<ul><li>业务绩效监控</li><li>模型监控</li><li>技术/系统监控</li><li>警示系统</li><li>自动重复训练</li></ul></li></ol><br>
<br>典型的机器学习周期包括以下阶段，子阶段和组件：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210816/754d8cbd0d62068d899c64cbc392d41c.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210816/754d8cbd0d62068d899c64cbc392d41c.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
让我们更详细地看一下每个阶段和组件以及相关的MLOps工具。<br>
<h3>数据和特征管理</h3><h4>数据储存</h4>机器学习工程师处理的数据来自各种各样的数据库。他们还可以处理第三方数据，API，电子表格，文本文件等数据。机器学习工作通常涉及在数据清理，提取主要数据，数据充实化等之后多个版本的数据。为了保留机器学习开发过程中的中间步骤生成的数据，可以使用下面提供的一个或多个数据存储：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210816/ce2c744a27160686b431768289526516.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210816/ce2c744a27160686b431768289526516.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>数据准备</h4>收集完数据后，下一步就是数据准备。这一步骤涉及基本的数据重组，格式化和清理。接下来是探索和分析以及提高数据质量。某些工作可以完全是手动的，而其余的可以自动化并且放入机器学习的某一个步骤之中。<br>
<h4>数据探索</h4>要连接到前面提到的数据源，您需要一种机器学习编程语言，一个好的代码编辑器（或IDE）来编写您的程序，以及专门为处理大量机器学习数据而构建的工具。在使用这些工具包的时候，您就可以开始探索数据，编写SQL查询以及构建PySpark 转换和开发机器学习模型。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210816/43f7401f747e14f6c5c340cd95354060.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210816/43f7401f747e14f6c5c340cd95354060.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>特征储存</h4>在清理，准备和分析数据之后，您可以开始构建特征储存，而这些特征储存是用于模型开发和建立（通常以表格形式）。我们可以在数据库，数据仓库，对象存储，本地实例等中创建它。<br>
<h3>模型开发</h3><h4>模型注册</h4>创建机器学习模型是一个增量过程。核心思想是不断改进模型，这就是为什么MLOps增加了另一个称为持续训练（CT）的功能。除了持续集成（CI）和持续部署（CD），持续训练对于机器学习的开发至关重要。要维护模型沿袭，源代码版本控制和注释，可以使用模型注册。<br>
<br>模型注册由前面提到的所有信息以及模型的所有其他可能的信息组成。您可以使用MLFlow模型注册或SageMaker模型注册之类的工具来存储有关模型的信息。<br>
<h4>元数据存储</h4>在机器学习流程的每个步骤中，每一个步骤都会做出决策；这些决策将传递到流程的下一步。机器学习元数据存储可帮助您存储和检索不同步骤中的元数据。元数据可帮助您追溯每一步所做的决策，使用的超参数以及用于训练模型的数据。您可以使用诸如Google的机器学习元数据（MLMD）和Kubeflow这一些的工具作为元数据存储。<br>
<h4>模型训练与验证</h4>您可以使用一个或多个“数据浏览”部分的资源来训练和验证模型。例如，如果您选择用Python编写代码，则可以访问特定的Python库进行模型的训练和验证，例如TensorFlow，PyTorch，Theano，PySpark等。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210816/31392fe5e4d8d6546c12133b79fd57fe.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210816/31392fe5e4d8d6546c12133b79fd57fe.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>版本控制</h4>在任何软件开发中，源代码版本控制都是最关键的领域之一。它可以使团队使用相同的代码，因此每个人都可以同时为进度做出贡献。几十年前，Subversion，Mercurial和CVS是主要的版本控制系统。现在，Git是版本控制标准。Git是可以安装在服务器上的开源软件（OSS）。您也可以选择使用基于云的服务。以下是一些主要产品：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210816/a44df962b794d14ff8e752b726003fe8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210816/a44df962b794d14ff8e752b726003fe8.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>机器学习的专用源代码控制</h4>您可能还需要查看数据版本控制（DVC），这是另一个用于源代码控制的开源软件工具，专门用于数据科学和机器学习项目。DVC是与Git兼容的，旨在通过使用基于DAG的格式对整个机器学习项目进行端到端的版本控制来支持机器学习开发。这有助于防止重复数据处理。<br>
<br>尽管Git是为版本化应用程序代码而编写的，但它并不意味着存储机器学习模型中使用到的大量数据或支持机器学习流水线。DVC已尝试解决这两个问题。DVC与存储层无关，可与GitHub，GitLab等任何源代码控制服务一起使用。<br>
<h3>模型运作</h3><h4>自动化测试</h4>机器学习以下有两种测试模型方法：<br>
<ol><li>测试模型的编码逻辑</li><li>测试模型的输出/准确性</li></ol><br>
<br>前者或多或少类似于测试软件应用程序，您应该以相同的方式使其自动化。但是，后者涉及测试模型的置信度，重要模型度量的性能等。机器学习测试通常以混合方式完成，其中一些测试是自动化的并且是流程中的一部分，而另一些则完全是非自动化的。<br>
<br>根据机器学习开发的阶段，测试可以分为两种不同的类型-训练前和训练后。<br>
<br>训练前测试不需要训练参数。这些测试可以检查（a）模型输出是否在特定的预期范围内，（b）机器学习模型的数据维数是否与数据集对齐。您可以手动执行许多测试。<br>
<br>训练后测试更具影响力，并且具有更多意义，因为它们针对模型而运行，这意味着机器学习模型已经在运行测试之前完成了工作。这使我们对模型的行为有了更深入的了解。<br>
<br>测试是开发过程中不可或缺的一部分。您可以在机器学习开发工作流程的各个阶段进行不同类型的测试。下面列出了一些可能的测试：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210816/747d34a457dc373d7d0e516c920e95d7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210816/747d34a457dc373d7d0e516c920e95d7.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>持续集成，部署和培训（CI/CD/CT）</h4>与在软件应用程序中将应用程序生成的数据与应用程序工件分离开来的软件不同，在机器学习开发中，训练数据从概念上讲是模型工件中非常重要的一部分。未经测试，您无法测试模型的有效性或良好性。这就是为什么通常的CI/CD流程通过向其添加另一个组件-持续测试而得以增强，从而促进了机器学习开发。代码集成和部署始终要经过培训。训练模型后，循环将继续。<br>
<h4>模型服务基础架构</h4>创建机器学习模型后，您必须决定将模型部署到何处。例如，将使用哪个平台来为机器学习模型提供服务。有许多选项可用于从本地服务器提供模型服务。本地服务器可能适用于某些用例。对于其他人，它可能会变得非常昂贵，并且难以大规模管理。或者，您可以使用一个或多个基于云的平台（例如AWS，Azure和GCP）来服务模型。<br>
<br>无论您使用本地服务器，云平台还是混合方法，您仍然可以选择将模型作为可执行文件直接部署到实例中。有许多尝试解决端到端机器学习模型服务问题的PaaS产品可选择。这通常是机器学习模型流程中的最后一步。此后，仍保留诸如模型监视之类的部署。<br>
<br>一些常见的部署选项是：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210816/fab1473982d5cd5863946da182944072.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210816/fab1473982d5cd5863946da182944072.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>模型监控</h3>监视模型涉及三个方面：<br>
<ol><li>技术/系统监视模型基础架构的行为是否正常，以及模型的服务是否正确。机器学习工程师需要通过跟踪服务级别指标，保证其符合服务级别协议</li><li>同时，模型监视需要监控模型输出数据，将输出与实际输入数据进行比较。模型监视是通过检查假正率和真负率，准确性，召回率，F1得分，R平方，偏差等来不断验证预测的准确性。</li><li>借助业务绩效监控，了解该模型是否对业务有所帮助。您需要能够监视各个团队进行的模型实验对业务的影响。您需要监视新一代模型发布后对业务的影响，并将其与以前的结果进行比较。</li></ol><br>
<br>在高度发达的MLOps工作流程中，监视应该是主动的，而不是被动的。您应同时为软件基础架构与机器学习模型定义服务级别目标，建立服务等级协定。监控服务级别目标，并跟踪其是否违反服务级别协议。这样做可以使您不断调整和改进模型。这是机器学习工作流程的最后一步，而且从这里开始重复开发周期。<br>
<h4>警示系统</h4>当今的系统是如此复杂，以至于手动进行监视是没有意义的。您需要软件来确定其他软件是否运行正常。您应该在监视数据上定义规则，而不是手动浏览应用程序日志，决策树和建议日志。规则基于服务级别目标和服务级别协议。违反规则条件时，可以设置触发器。例如：<br>
<ol><li>向诸如PagerDuty之类的寻呼机应用程序发送推送通知。</li><li>使用协作通信工具（如Slack，Microsoft Teams等）发送警报。</li><li>发送电子邮件或短信。</li></ol><br>
<br>您发送警报的渠道取决于您用于管理生产问题的应用程序和流程。警报需要谨慎处理；否则，它会发送过多的警报，从而使之陷入困境。降低错误警报具有挑战性。您需要做出有意识的，周到的选择，以使警报系统正常运行。<br>
<h4>自动重复训练</h4>机器学习模型只有在不断重复训练的情况下，才保持相关性。当有新的真实数据输入到系统中，并且针对真实输出与模型预测输出对比时，便可以对模型进行重复训练。监视为警报引擎提供了信息，但您也可以将监视系统配置为提供模型本身，从而创建贯穿整个机器学习周期的反馈循环。这将是机器学习模型可以获得的最有价值的反馈，因为该反馈是在生产部署之后发出的。<br>
<br>根据数据模型的实现或项目的体系结构，许多新的范例（如AutoML，AutoAI，自整定系统）变得非常重要。您可以从多种适合您需求的工具中选择一种，并找到一种有效的方法来重新训练模型。请记住，模型重复训练不会导致代码更改；它仅提供新的生产数据并将机器学习的模型输出提供给机器学习模型本身。<br>
<h3>结论</h3>本文研究了MLOps如何适应机器学习周期。我们还研究了在开发，部署和服务机器学习模型时需要了解和使用的各种工具。在评估MLOps工具时，大多数工具都是相对较新的，因此几乎没有端到端工作流。机器学习团队应根据自身需求选择适用的MLOps平台与工具。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/sHSnzdP-Cl-OMAN0ho3afg" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/sHSnzdP-Cl-OMAN0ho3afg</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            