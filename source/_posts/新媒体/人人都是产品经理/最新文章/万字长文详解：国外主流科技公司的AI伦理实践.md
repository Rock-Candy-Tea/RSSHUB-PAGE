
---
title: '万字长文详解：国外主流科技公司的AI伦理实践'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2022/03/1X7vE8q1kCK5tLlNr9Hi.png'
author: 人人都是产品经理
comments: false
date: Wed, 09 Mar 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/03/1X7vE8q1kCK5tLlNr9Hi.png'
---

<div>   
<blockquote>
<p style="text-align: left;">编辑导语：AI是近两年国内外的热门话题，各大科技公司纷纷把AI伦理和可信AI作为市场竞争的核心优势。本篇文章中，作者分析了微软、谷歌、IBM、Twitter四家大牌互联网公司，在AI方面的发展。感兴趣的小伙伴不妨来看看。</p>
</blockquote>
<p><img data-action="zoom" class="size-full wp-image-765637 aligncenter" src="https://image.yunyingpai.com/wp/2022/03/1X7vE8q1kCK5tLlNr9Hi.png" alt referrerpolicy="no-referrer"></p>
<p>2022年全国两会期间，社会各界热议科技创新与科技伦理。</p>
<p>从业界具体实践来看，随着各界对AI伦理的日益重视和各国AI监管政策和立法的持续推进，各大科技公司纷纷拥抱AI伦理，打造可信AI，把AI伦理和可信AI作为打造AI产品和服务的市场竞争优势的核心引擎之一。</p>
<p>微软、谷歌、IBM、Twitter等众多国外主流科技公司在AI伦理与可信AI方面谋划早、布局全、实践深，涉及原则、治理机构、技术工具和解决方案、AI伦理产品服务、行动指南、员工培训等诸多层面。</p>
<p><strong>本文对微软、谷歌、IBM、Twitter这四家比较有代表性的公司的实践做法予以系统梳理，以期能够有所启示。</strong></p>
<h2 id="toc-1">一、微 软</h2>
<h3>1. 伦理原则</h3>
<p>微软致力于以人为本地推动AI技术发展，在AI伦理方面提出公平、安全可靠、隐私保障、包容、透明、负责六大原则。</p>
<h3>2. 治理机构</h3>
<p>微软主要有三个内设机构负责AI伦理践行方面的事务。</p>
<p>它们分别是负责任人工智能办公室（Office of Responsible AI，以下简称ORA），人工智能、伦理与工程研究委员会（AI and ethics in engineering and research committee，以下简称Aether committee），以及负责任AI战略管理团队（Responsible AI Strategy in Engineering，以下简称RAISE）。</p>
<p>ORA主要有四个职能：</p>
<ol>
<li>制定公司内部的负责任AI规则；</li>
<li>团队赋能，帮助公司以及客户落实AI伦理规则；</li>
<li>审查敏感用例，确保微软AI原则在开发和部署工作中得到实施；</li>
<li>推进立法、规范、标准的制定，确保人工智能技术有助于提升社会福祉。</li>
</ol>
<p>通过这些行动，人工智能办公室将微软的AI伦理原则付诸实践。</p>
<p>Aether于2017年设立，该委员会由产品开发、研究员、法律事务、人力资源等部门的负责人组成。</p>
<p>专注于公平与包容、安全可靠、透明可解释、隐私保障、人工智能交互协作领域，积极制定内部政策，并决定怎样负责任地处理出现的问题。</p>
<p>当部门内部出现问题时，委员会以研究、反思和建议来回应，这些针对特定案例的建议可能演变为公司通用的理念、政策和实践。</p>
<p>RAISE旨在使负责任AI的要求整合到团队日常开发过程中。</p>
<p>其有三项职能：</p>
<ol>
<li>建立负责任AI的工具和系统，帮助公司及客户实现AI伦理落地；</li>
<li>帮助工作团队落实负责任AI规则，将负责任AI的要求整合到日常工作中；</li>
<li>为工程团队提供合规工具，以监控和执行负责任AI规则的要求。</li>
</ol>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="收藏｜万字长文详解：国外主流科技公司的AI伦理实践" src="https://image.yunyingpai.com/wp/2022/03/VJmNBm3rWpZnLTm6AGws.png" alt="收藏｜万字长文详解：国外主流科技公司的AI伦理实践" width="600" height="204" referrerpolicy="no-referrer"></p>
<h3>3. AI伦理的技术解决方案</h3>
<p>针对AI伦理实践，微软给出了一系列的技术解决方案。</p>
<p>这些技术解决方案包括了贯穿整个AI生命周期的技术工具（Technology tools）和管理工具（Management tools）。</p>
<p>同时，还包括了按照应用场景将需求特性集成到AI系统中的工具包（Toolkit）。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="收藏｜万字长文详解：国外主流科技公司的AI伦理实践" src="https://image.yunyingpai.com/wp/2022/03/6A0jRadXYGFXKGinBEcz.png" alt="收藏｜万字长文详解：国外主流科技公司的AI伦理实践" width="600" height="351" referrerpolicy="no-referrer"></p>
<p><strong>（1）</strong><strong>技术工具</strong></p>
<p><strong>① 评估</strong></p>
<p>Fairlearn：一个python工具包/库，用于评估给定AI模型在一系列公平性指标上的得分。</p>
<p>如”预测个人收入“的模型是否在男性客户群体中的预测效果比女性群体更好，进而发现可能的模型歧视，为模型的改进提供公平性约束。</p>
<p>InterpreteML：一个python工具包/库， 集成了一系列XAI（可解释AI）的前沿方法。</p>
<p>既允许用户从头训练一个可解释的“玻璃箱”模型，还能帮助人们理解/解释某些给定的”黑箱”模型。</p>
<p>Error Analysis：一个python工具包/库，提供一系列对于主流AI模型进行“错误分析”的功能。</p>
<p>包括但不限于为误分类样本建立可视化热力图，构建全局/局部解释，因果干涉等分析，帮助人们更好探索数据、认识模型。</p>
<p>Counterfit：一个基于命令行的通用检测工具，用于测试给定的AI系统在作为开源平台时的稳定性和安全性。</p>
<p><strong>② 开发</strong></p>
<p>SamrtNoise：一系列基于“差分隐私”的前沿AI技术：通过特定方式在AI模型训练过程中添加噪音，确保开发者在开发过程中、所用敏感隐私数据不会泄露。</p>
<p>Presidio：一个python工具包/库。能帮助使用者高效地识别、管理并模糊大数据中的敏感信息，比如自动识别文本中的地址、电话等。</p>
<p><strong>③ 部署</strong></p>
<p>Confidential computing for ML：在微软云的系统上，通过机密计算等系统层面的安全手段，保证模型与敏感数据的绝对安全。</p>
<p>SEAL Homomorphic Encryption：使用开源同态加密技术，允许在加密数据上执行计算指令，同时防止私有数据暴露给云运营商。</p>
<p><strong>（2）</strong><strong>管理工具</strong></p>
<p>AI fairness checklist：AI fairness checklist研究项目探讨如何设计人工智能道德清单，以支持更公平的人工智能产品和服务的发展。</p>
<p>研究小组与清单的使用者——人工智能从业人员协作，征求他们的意见，形成人工智能的设计、开发和部署全生命周期的检查清单。</p>
<p>项目的首批研究已经产生了一个与从业者共同设计的公平性清单，同时也形成了对组织和团队流程如何影响AI团队解决公平性危害的见解。</p>
<p>HAX Playbook：一个主动、系统地探索常见人工智能交互故障的工具。</p>
<p>Playbook 列出了与人工智能产品应用场景相关的故障，以便为开发者提供有效恢复的方法。</p>
<p>Playbook 还提供了实用的指导和示例，以说明如何用较低的成本模拟系统行为，以便进行早期用户测试。</p>
<p>Datasheets for Datasets：机器学习社区目前没有记录数据集的标准化流程，这可能会导致高风险领域的严重后果。</p>
<p>为了解决这个差距，微软开发了Datasheets for Datasets。</p>
<p>在电子工业中，每一个组件，无论多么简单或复杂，都有一个数据表（datasheet）来描述其操作特性、测试结果、推荐用途和其他信息。</p>
<p>相应的，每一个数据集（dataset）都应该有一个记录其动机、组成、收集过程、推荐用途等的数据表。</p>
<p>Datasheets for Datasets将促进数据集创建者和数据集消费者之间的沟通，并鼓励机器学习优先考虑透明度和问责制。</p>
<p><strong>（3）</strong><strong>工具包</strong></p>
<p>Human AI eXperience（HAX）Toolkit：HAX Toolkit是一套实用工具，旨在帮助AI创造者，包括项目管理和工程团队等主体，在日常工作中采用这种以人为本的方法。</p>
<p>Responsible AI Toolbox：Responsible AI Toolbox涵盖了错误分析（Error Analysis）、可解释性（Interpretability）、公平性（Fairness）、负责任（Responsible）四个界面。</p>
<p>增进人们对AI系统的了解，使开发者、监管机构等相关人员能够更负责任地开发和监控 AI，并采取更好的数据驱动行动（data-driven actions）。</p>
<h3>4. 行动指南</h3>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="收藏｜万字长文详解：国外主流科技公司的AI伦理实践" src="https://image.yunyingpai.com/wp/2022/03/nl5Eqm6bl1OdSJWBGuN1.png" alt="收藏｜万字长文详解：国外主流科技公司的AI伦理实践" width="600" height="906" referrerpolicy="no-referrer"></p>
<p>为了能让项目团队更好地贯彻AI原则，微软公司发布了一系列行动指南（Guidelines），在项目开发过程中为团队提供具体的行动建议、解决方案。</p>
<p>如“应该收集哪些数据”、“应该如何训练AI模型”等问题上。</p>
<p>行动指南旨在为团队节省时间、提高用户体验、贯彻AI伦理原则。</p>
<p>行动指南不同于任务清单（checklist），或许并不适用于每一个应用场景，也并非需要团队强制遵守。</p>
<p>针对特殊情况、专门领域，会发布专用的行动指南。</p>
<p>微软针对人工智能交互问题、安全问题、偏见问题、机器人开发领域问题，发布了6项行动指南，贯穿负责任AI的评估环节、开发环节。</p>
<p>其中HAX Workbook、Human AI Interaction Guidelines以及HAX Design Patterns旨在帮助解决人工智能交互问题；</p>
<p>AI Security Guidance针对人工智能可能带来的安全威胁，提供解决方案；</p>
<p>Inclusive Design Guidelines充分考虑了人类的多样性，用于解决AI可能带来的偏见问题；</p>
<p>Conversational AI guidelines专注于机器人开发领域可能带来的种种问题。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="收藏｜万字长文详解：国外主流科技公司的AI伦理实践" src="https://image.yunyingpai.com/wp/2022/03/Nsfk1U8wk0mKwBV2vTyh.png" alt="收藏｜万字长文详解：国外主流科技公司的AI伦理实践" width="600" height="216" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、谷 歌</h2>
<h3>1. 伦理原则</h3>
<p>谷歌从积极方面和消极方面规定了人工智能设计、使用的原则，将其作为公司和未来AI发展的基础。</p>
<p>该原则以“道德宪章”的地位，指导公司的AI研究以及AI产品中的开发和使用。</p>
<p>同时谷歌也承诺，愿意随着时间的推移而及时调整这些原则。</p>
<p>具体来说，这些原则包括：</p>
<p>积极方面，人工智能的使用应该：</p>
<ol>
<li>有利于增进社会福祉；</li>
<li>避免制造或强化歧视、偏见；</li>
<li>以安全为目的的创新；</li>
<li>对公众负责；</li>
<li>纳入隐私设计原则；</li>
<li>坚持科学卓越的高标准；</li>
<li>符合这些原则。</li>
</ol>
<p>消极方面，公司不会在以下应用领域设计或部署AI：</p>
<ol>
<li>造成或可能造成危害的技术；</li>
<li>对人造成伤害的武器或其他技术；</li>
<li>违反了国际公认规范，收集或使用信息用于监视的技术；</li>
<li>目的违反广泛接受的国际法和人权原则的技术。</li>
</ol>
<h3>2. 治理机构</h3>
<p>2018年，谷歌宣布人工智能原则的同时，成立了负责任创新中央团队（central Responsible Innovation team），当初这个团队仅由6名员工组成。</p>
<p>如今，团队规模已经显著扩大，数百名谷歌员工构成了数十个创新团队，在人权、用户体验研究、伦理、信任和安全、隐私、公共政策、机器学习等领域构建了一个AI原则生态系统。</p>
<p>谷歌通过这个内部的AI原则生态系统来实施负责任AI的创新实践，帮助谷歌技术开发人员将负责任AI落实到他们的工作当中。</p>
<p>这个生态系统的核心是一个三层的治理架构：</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="收藏｜万字长文详解：国外主流科技公司的AI伦理实践" src="https://image.yunyingpai.com/wp/2022/03/bTbyIE5klNqjryA1A072.png" alt="收藏｜万字长文详解：国外主流科技公司的AI伦理实践" width="600" height="348" referrerpolicy="no-referrer"></p>
<p>第一层是<strong>产品团队</strong>，由专门负责用户体验（UX）、隐私、信任和安全（T&S）等方面的专家组成，这些专家提供与人工智能原则相一致的专业知识。</p>
<p>第二层是专门的审查机构和专家团队。</p>
<p>由负责任创新中央团队（Central Responsible Innovation Review Committee）、隐私顾问委员会（Privacy Advisory Council）、卫生伦理委员会（Health Ethics Committee）以及产品审查委员会（Product Area AI Principles Review Committees）四个部门组成。</p>
<p><strong>（1）负责任创新中央团队</strong>（Central Responsible Innovation Review Committee）</p>
<p>该团队为整个公司的实施AI原则提供支持。</p>
<p>公司鼓励所有员工在整个项目开发过程中参与人工智能原则的审查。</p>
<p>一些产品领域已经建立了审查机构，以满足特定的受众和需求。</p>
<p>如谷歌云（Google Cloud）中的企业产品、设备和服务（Devices and Services）中的硬件、谷歌健康（Google Health）中的医学知识。</p>
<p><strong>（2）隐私顾问委员会</strong>（Privacy Advisory Council）</p>
<p>该委员会负责审查所有可能存在潜在隐私问题的项目，包括（但不仅限于）与人工智能相关的问题。</p>
<p><strong>（3）健康伦理委员会</strong>（Health Ethics Committee）</p>
<p>HEC成立于成立于2020年，是一个在健康领域发挥指导、决策功能的论坛，针对健康产品、健康研究或与健康有关的组织决策等领域产生的伦理问题提供指导，保护谷歌用户和产品的安全。</p>
<p>HEC是一个综合性的论坛，其中包括生物伦理学、临床医学、政策、法律、隐私、合规、研究和商业方面的主题专家。</p>
<p>2021年，谷歌生物伦理项目创建了the Health Ethics Cafe，这是一个讨论生物伦理问题的非正式论坛。</p>
<p>公司任何人在项目开发的任何阶段都可以在此进行讨论，论坛中遇到的棘手问题将被升级到HEC进行审查。</p>
<p><strong>（4）产品审查委员会</strong>（Product Area AI Principles Review Committees）</p>
<p>PAAPRC是一个专门为特定产品领域而设立的审查委员会。</p>
<p>其中包括谷歌云的负责任AI产品委员会（Responsible AI Product Committee）和交易审查委员会（Responsible AI Deal Review Committee）。</p>
<p>其旨在确保谷歌云的AI产品、项目以系统、可重复的方式与谷歌人工智能原则保持一致，并将道德、责任嵌入了设计过程中。</p>
<p>产品委员会专注于云人工智能和行业解决方案（Cloud AI & Industry Solutions）所构建的产品。</p>
<p>根据AI原则对社会技术前景、机会以及危害进行综合审查，并与跨职能、多样化的委员会进行现场讨论，从而形成一个可操作的协调计划。</p>
<p>交易审查委员是一个由四名跨职能的高级执行成员组成的委员会。</p>
<p>所有决定的作出都必须得到所有四名委员会成员的完全同意，并根据需要逐步升级。</p>
<p>谷歌AI原则生态系统的相关人员会帮助委员会了解讨论的内容，避免其凭空做出决定。</p>
<p>第三层是<strong>先进技术审查委员会</strong>（Advanced Technology Review Council）。</p>
<p>这是一个由高级产品、研究和商业主管轮流担任委员的委员会，代表着谷歌公司多个部门的不同意见。</p>
<p>ATRC处理升级问题以及最复杂的先例性案例，并建立影响多个产品领域的策略，权衡潜在的商业机会和某些应用程序的道德风险。</p>
<p><strong>案例一：谷歌云的负责任AI产品审查委员会&谷歌云负责任AI交易审查委员会为避免加重算法不公平或偏见，决定暂停开发与信贷有关的人工智能产品</strong></p>
<p>2019年，谷歌云的负责任AI产品审查委员会评估了信用风险和信誉领域的产品。</p>
<p>虽然我们希望有一天AI能够进入信贷领域，并在增进金融普惠和财务健康方面发挥作用。</p>
<p>但产品审查委员会最终否定了这项产品——用当下的技术、数据打造的信用可靠性产品，可能在性别、种族和其他边缘化群体方面产生差别影响，并与谷歌“避免创造或加强不公平的偏见”的人工智能原则相冲突。</p>
<p>2020年年中，产品审查委员会重新评估并重申了这一决定。</p>
<p>在过去的一整年中，交易审查委员会评估了多个与信贷评估有关的人工智能应用（proposed custom AI engagements）。</p>
<p>每一项应用都会根据其特定的用例进行评估，交易审查委员会最终决定拒绝进行其中的许多业务。</p>
<p>多年的经验和教训让我们确信：在风险得到适当缓解之前，应该暂停开发与信贷相关的定制AI解决方案（custom AI solutions）。</p>
<p>这个方针从去年开始生效，并一直持续到今天。</p>
<p><strong>案例二：先进技术审查委员会基于技术问题与政策考量，拒绝通过面部识别审提案</strong></p>
<p>2018年，先进技术审查委员会处理了谷歌云产品的审查提案，决定在解决重大技术、政策问题之前，不提供通用面部识别API，并建议团队专注于专用AI解决方案。</p>
<p>随后，公司内外相关人员对此进行了大量的投入。</p>
<p>经过团队的多年努力，谷歌云开发了一个高度受约束的名人专用API2（Celebrity Recognition API2），并寻求ATRC的批准，最终ATRC同意发布该产品。</p>
<p><strong>案例三：先进技术审查委员会对涉及大型语言模型的研究进行审查，认为其可以谨慎地继续</strong></p>
<p>2021年，先进技术审查委员会审查的其中一个主题是关于大型语言模型的发展。</p>
<p>审查之后，先进技术审查委员会决定，涉及大型语言模型的研究可以谨慎地继续，但在进行全面的人工智能原则审查之前，此模型不能被正式推出。</p>
<h3>3. 技术工具</h3>
<p><strong>（1）Fairness Indicators：</strong>2019年发布，用于评估产品的公平性。Min-Diff14 technique：对日益增多的产品用例进行补救，以达到最佳的学习规模，能够主动解决公平性问题。</p>
<p><strong>（2）federated learning：</strong>在Gboard等产品中使用的联邦学习，帮助模型根据真实的用户交互进行集中训练和更新，而无需从个人用户那里收集集中的数据，以增强用户隐私。</p>
<p><strong>（3）federated analytics：</strong>使用与federated learning类似的技术，在不收集集中数据的情况下，深入了解产品特性和模型对不同用户的性能。</p>
<p>同时，federated analytics也允许项目团队在不访问原始用户数据的情况下进行公平性测试，以增强用户隐私。</p>
<p><strong>（4）federated reconstruction：</strong>与模型无关的方法，可以在不访问用户隐私信息的情况下，实现更快、大规模的联邦学习。</p>
<p><strong>（5）Panda：</strong>一种机器学习算法，帮助谷歌评估网站的整体内容质量，并相应地调整其搜索排名。</p>
<p><strong>（6）Multitask Unified Model (MUM)：</strong>使搜索引擎理解各种格式的信息，如文本、图像和视频，并在我们周围世界的概念、主题和想法之间建立隐含的联系。</p>
<p>应用MUM不仅将帮助世界各地的人们更高效地找到他们所需要的信息，而且还将增强创造者、出版商、初创企业和小企业的经济效益。</p>
<p><strong>（7）Real Tone：</strong>为深色肤色的用户提供了人脸检测、自动曝光和自动增强等功能，帮助人工智能系统发挥更好性能。</p>
<p><strong>（8）Lookout：</strong>一款为盲人和低视力者开发的安卓应用程序，使用计算机视觉技术提供用户周围的环境信息。</p>
<p><strong>（9）Project Relate：</strong>使用机器学习来帮助有语言障碍的人更便利地交流以及使用科技产品。</p>
<p><strong>（10）Privacy Sandbox：</strong>与广告行业合作，在支持出版商、广告商和内容创造者的同时，通过AI技术增强用户隐私，提供更私密的用户体验。</p>
<h3>4. 产品与服务</h3>
<p><strong>（1）Google Cloud：</strong>为各行业大规模应用可信赖AI模型，提供可靠的基础设施与高效的部署方案，并配套提供员工培训、集成相关开发环境等服务，使得各行业人员能更便捷地掌握和使用可信赖的AI工具模型。</p>
<p><strong>（2）TensorFlow：</strong>世界上最流行的ML框架之一，拥有数百万的下载量和全球开发者社区，它不仅在谷歌中被使用，而且在全球范围内被用来解决具有挑战性的现实世界问题。</p>
<p><strong>（3）</strong><strong>Model Cards</strong><strong>：</strong>一种情景假设分析工具，能够为AI的算法运作提供一份可视化的解释文档。</p>
<p>该文档能够为使用者阅读，使其充分了解算法模型的运作原理和性能局限。</p>
<p>从技术原理上看，模型卡片设置的初衷是以通俗、简明、易懂的方式让人类看懂并理解算法的运作过程。</p>
<p>其实现了两个维度的“可视化”：</p>
<ol>
<li>显示算法的基本性能机制；</li>
<li>显示算法的关键限制要素。</li>
</ol>
<p><strong>（4）Explainable AI：</strong>借助该服务，客户可以调试和提升模型性能，并帮助他人理解客户的模型行为。</p>
<p>还可以生成特征归因，以在AutoML Tables和Vertex AI中进行模型预测，并利用 What-If 工具以直观的方式调查模型行为。</p>
<h3>5. 治理创新：重视员工培训</h3>
<p>相比于其他企业，谷歌在AI伦理实践方面的一大特色是专为员工开设了科技伦理培训（Technology ethics training）。</p>
<p>该培训项目旨在通过科技哲学来指导员工遵循道德，使他们了解如何评估潜在的利害。</p>
<p>同时还配有课程，为员工解释谷歌人工智能原则和内部治理实践。</p>
<p>不仅如此，2021年，谷歌还为新员工配套了AI原则和负责任创新培训课程（AI Principles and responsible innovation training course），帮助他们了解谷歌的伦理道德准则和可用资源。</p>
<p>2021年，谷歌还推出了在线互动答题（interactive online puzzles），旨在帮助员工建立对人工智能原则的认识，并测试他们的记忆程度。</p>
<h2 id="toc-3">三、IBM</h2>
<h3>1. 伦理原则</h3>
<p>IBM针对AI伦理问题提出了三大原则、五大支柱。</p>
<p>三大原则分别是：</p>
<ol>
<li>人工智能的目的是增强人类的智慧</li>
<li>数据和观点都属于它们的创造者</li>
<li>技术必须是透明和可解释的。</li>
</ol>
<p>五大支柱分别是：</p>
<ol>
<li>公平性</li>
<li>可解释性</li>
<li>鲁棒性</li>
<li>透明性</li>
<li>隐私性</li>
</ol>
<h3>2. 治理机构</h3>
<p>IBM在AI伦理践行方面主要由AI伦理委员会（AI Ethics Board）负责，公司AI治理框架的所有核心内容均处于AI伦理委员会之下。</p>
<p>委员会负责制定指导方针，并为人工智能的设计、开发和部署工作保驾护航，旨在支持整个公司的所有项目团队执行AI伦理原则，并敦促公司和所有员工坚守负责任AI的价值观。</p>
<p>该委员会是一个跨学科的中央机构，委员会成员包括来自公司各个部门的代表，针对业务部门、科研部门、营销部门、宣传部门等部门的工作制定决策。</p>
<p>此外，委员会还帮助业务部门了解对技术特征的预期，帮助公司各部门在AI伦理领域做到相互熟悉和了解，以便更好地开展协作。</p>
<p>同时，AI伦理委员会还将依据公司AI原则、具体核心内容以及技术特征，审查业务部门可能向客户提供的新产品或服务的提案。</p>
<p>审查未来可能与客户达成的交易时，委员会主要关注以下三个方面：</p>
<ol>
<li>首先是技术特征，</li>
<li>其次是技术的应用领域，</li>
<li>最后是客户本身，即审查客户以往是否妥善遵循负责任AI原则。</li>
</ol>
<p><strong>案例一：新冠疫情期间，AI伦理委员会参与数字健康通行证开发、部署阶段的评审工作。</strong></p>
<p>为协助新冠疫情治理，IBM制定了数字健康通行证（Digital Health Pass）。</p>
<p>该通行证的开发团队从最早的概念阶段开始，就向委员会征询意见。</p>
<p>该通行证是通用的“疫苗护照（vaccine passports）”可能导致隐私问题或不公平的访问。</p>
<p>因此IBM的解决方案是：只有在个人同意后才能共享个人信息，并使每个人都受益。委员会参与了开发阶段，并在部署解决方案时继续进行评审。</p>
<h3>3. 技术解决方案</h3>
<p>IBM根据AI伦理的五大支柱：</p>
<ol>
<li>可解释性</li>
<li>公平性</li>
<li>鲁棒性</li>
<li>透明性</li>
<li>隐私性</li>
</ol>
<p>提出了五种针对性的技术解决方案。相应的，它们分别是：</p>
<ol>
<li>AI Explainability 360 toolkit</li>
<li>AI Fairness 360 toolkit</li>
<li>Adversarial Robustness 360 Toolbox v1.0</li>
<li>AI FactSheets 360</li>
<li>IBM Privacy Portal</li>
</ol>
<p><strong>（1）AI Explainability 360 toolkit</strong></p>
<p>从普通人到政策制定者、从科研人员到工程技术人员，不同的行业和角色需要各不相同的可解释性。</p>
<p>为了有效解决可解释性多样性、个性化的强烈需求，IBM的研究人员提出了集成可解释性工具箱AI Explainability 360（AIX360）。</p>
<p>这一开源工具箱涵盖了八种前沿的可解释性方法和两个维度评价矩阵。</p>
<p>同时还提供了有效的分类方法引导各类用户寻找最合适的方法进行可解释性分析。</p>
<p><strong>（2）AI Fairness 360 toolkit</strong></p>
<p>人工智能算法中的偏差问题越来越受到关注，AI Fairness 360是解决这一问题的开源解决方案。</p>
<p>该工具提供了算法，使开发人员能够扫描最大似然模型，以找到任何潜在的偏见。</p>
<p>这是打击偏见的一个重要工作，当然也是一项复杂的任务。</p>
<p><strong>（3）Adversarial Robustness 360 Toolbox v1.0</strong></p>
<p>ART最初于2018年4月发布，是一个对抗性机器学习的开源库，为研究人员和开发人员提供最先进的工具，以在对抗性攻击面前防御和验证人工智能模型。</p>
<p>ART解决了人们对人工智能日益增加的信任担忧问题，特别是在关键任务应用中人工智能的安全性。</p>
<p><strong>（4）AI FactSheets 360</strong></p>
<p>以AI事实清单为代表的自动化文档是增强AI可解释性的重要方式，它能够以一种清晰明了的方式，作为技术人员与使用者的沟通介质，从而能避免许多情形下的道德和法律问题。</p>
<p>AI事实清单并不试图解释每个技术细节或公开有关算法的专有信息，它最根本的目标是在使用、开发和部署AI系统时，加强人类决策，同时也加快开发人员对AI伦理的认可与接纳，并鼓励他们更广泛地采用透明性可解释文化。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="收藏｜万字长文详解：国外主流科技公司的AI伦理实践" src="https://image.yunyingpai.com/wp/2022/03/xxK4917jqyCYRTVSzN8b.png" alt="收藏｜万字长文详解：国外主流科技公司的AI伦理实践" width="600" height="355" referrerpolicy="no-referrer"></p>
<h3>4. 行动指南</h3>
<p>IBM发布了《人工智能日常伦理指南》（Everyday Ethics for Artificial Intelligence），用于贯彻落实IBM提出的AI伦理道德原则。</p>
<p>该指南旨在让人工智能系统的设计者和开发人员系统地考虑AI伦理问题，将道德、伦理贯彻在AI的全生命流程中。</p>
<h2 id="toc-4">四、Twitter</h2>
<h3>1. 治理机构</h3>
<p>META团队（MachineLearning Ethics, Transparency & Accountability）：这是一个由公司内部的工程师、研究人员和数据科学家组成的专门小组。</p>
<p>主要工作是评估公司使用的算法造成或可能造成的无意伤害，并帮助Twitter确定待处理问题的优先级。</p>
<p>META团队致力于研究人工智能系统的工作原理，并改善人们在Twitter上的体验。</p>
<p>比如删除一种算法，让人们对自己发布的图片有更多的控制权，或者当这些图片对某个特定社区产生巨大影响时，Twitter会制定新的标准来设计和制定政策。</p>
<p>META团队工作的成果可能并不总是转化为可见的产品变化，但在机器学习的构建和应用上给我们带来更高层次的认知，并对重要问题作出讨论。</p>
<p><strong>案例一：对性别和种族偏见的深入研究</strong></p>
<p>META团队正在对图像裁剪算法中的性别和种族偏见进行“深入分析和研究”，其中包括对图像裁剪（显著性）算法的性别和种族偏见分析，对不同种族亚群体的“主页”时间线推荐内容进行公平性评估以及针对七个国家不同政治意识形态的内容推荐分析。</p>
<p><strong>二、治理创新：算法赏金挑战赛</strong></p>
<p>颇有意思的是，为解决ML图像裁剪的公平性问题，Twitter举办算法赏金挑战赛，使用社区主导的方法来构建更好的算法，收集来自不同群体的反馈。</p>
<p>2021 年 8 月，Twitter举办了第一次算法偏见赏金挑战赛，并邀请邀请人工智能开发者社区来拆解算法，以识别其中的偏见和其他潜在危害。</p>
<p>算法赏金挑战赛帮助公司在短时间内发现了算法对于不同群体的偏见问题，成为公司征求反馈和了解潜在问题的重要工具。</p>
<h2 id="toc-5">五、几点启示</h2>
<p>在这样一个新技术新应用新业态以指数级增长的数字化时代，由于技术与人之间的交互和相互影响不断加深，以及技术越来越具有更高的自主性，技术伦理成为了数字商业伦理的最新命题。</p>
<p>正如微软总裁兼副董事长布拉德·史密斯在其著作《工具，还是武器？》中所言，”如果你掌握了能够改变世界的科技，那么你就有责任帮助解决你创造的世界所面临的问题。”</p>
<p>我国的相关顶层政策文件和立法都对科技伦理提出了新的要求，强调科技伦理审查的重要性，塑造科技向善的文化理念。</p>
<p>在这样的背景下，微软、谷歌、IBM、Twitter等国外科技公司在AI伦理和可信AI上的实践做法，可以提供很多有意义的启发。</p>
<p>其一，在一个高度技术化、数字化的社会，在公司的治理版图上，技术伦理将成为与财务、法务等既有板块同等重要甚至更为重要的板块。</p>
<p>我们看到，技术伦理作为商业伦理的新拼图，越来越多的科技公司开始将首席伦理官、伦理委员会等机制内化为常态化的组织架构，统筹推进相关工作。</p>
<p>其二，AI伦理和可信AI需要系统化的建设，抽象的原则和顶层的框架固然重要，但行胜于言，更重要的是将伦理原则转化为具体的实践，融入技术设计以打造负责任的技术应用。</p>
<p>在这方面，内部治理机制、技术解决方案、伦理培训、伦理黑客社区（类似于网络安全领域的白帽黑客）、技术标准等传统的和创新性的方式日益发挥出重要作用。</p>
<p>因为可信AI和AI伦理不仅是理念原则，更是行动路线。</p>
<p>其三，正如可信AI和AI伦理的概念本身所表征的那样，我们需要反思技术人员主导的技术研发应用和部署过程，更多强调技术开发应用中的多元背景和多元参与。</p>
<p>将政策、法律、伦理、社会、哲学等领域的人员引入开发团队，是将伦理要求嵌入技术设计开发的最直接的、最有效的路径。</p>
<p>好的技术不仅关注结果，更要关注过程。</p>
<p>科技向善是高度技术化社会的终极愿景。科技向善（techforgood）的理念至少包括两个路径，向外需要用技术解决各种社会问题挑战，向内需要关注技术本身，打造“善的/好的技术”（goodtech）。</p>
<p>AI伦理和可信AI正是聚焦于如何打造“善的/好的技术”，最终为向外发力的“科技向善”建立基础。</p>
<p>参考文献：</p>
<p>[1]https：//www.microsoft.com/en-us/ai/responsible-ai?activetab=pivot1%3aprimaryr6</p>
<p>[2]https：//www.microsoft.com/en-us/ai/our-approach?activetab=pivot1%3aprimaryr5</p>
<p>[3]https：//www.microsoft.com/en-us/ai/responsible-ai-resources</p>
<p>[4]https：：//azure.microsoft.com/en-us/solutions/devops/devops-at-microsoft/one-engineering-system/</p>
<p>[5]https：//ai.google/responsibilities/</p>
<p>[6]https：//cloud.google.com/responsible-ai</p>
<p>[7]https：//www.tensorflow.org/responsible_ai</p>
<p>[8]https：//blog.tensorflow.org/2020/06/responsible-ai-with-tensorflow.html</p>
<p>[9]https：//github.com/microsoft/responsible-ai-toolbox</p>
<p>[10]https：//www.ibm.com/artificial-intelligence/ethics</p>
<p>[11]https：//aix360.mybluemix.net/?_ga=2.38820964.651461218.1639109085-1605157021.1638780204</p>
<p>[12]https：//www.ibm.com/blogs/research/2019/09/adversarial-robustness-360-toolbox-v1-0/</p>
<p>[13]https://blog.twitter.com/en_us/topics/company/2021/introducing-responsible-machine-learning-initiative</p>
<p>[14]https://blog.twitter.com/engineering/en_us/topics/insights/2021/algorithmic-bias-bounty-challenge</p>
<p> </p>
<p>作者：曹建峰、梁竹；公众号：腾讯研究院</p>
<p>本文由@ 腾讯研究院 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5347706" data-author="757351" data-avatar="http://image.woshipm.com/wp-files/2018/09/DYbfW4923k2EK5VH2paQ.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            