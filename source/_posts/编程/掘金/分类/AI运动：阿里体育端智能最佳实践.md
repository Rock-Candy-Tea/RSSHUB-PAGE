
---
title: 'AI运动：阿里体育端智能最佳实践'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90a9cf5fbff24b10a517d55ae4f43ee1~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 15 Jul 2021 18:51:02 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90a9cf5fbff24b10a517d55ae4f43ee1~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>简介：</strong> 过去一年，阿里体育技术团队在端智能方面不断探索，特别在运动健康场景下实现了实践落地和业务赋能，这就是AI运动项目。AI运动项目践行运动数字化的理念，为运动人口的上翻提供了重要支撑，迈出了阿里体育端智能运动领域的第一步，为用户带来了更加有趣的新颖玩法。上线以来，项目受到了广泛关注。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90a9cf5fbff24b10a517d55ae4f43ee1~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>作者 | 其声<br>
来源 | 阿里技术公众号</p>
<h3 data-id="heading-0">一 背景</h3>
<p>过去一年，阿里体育技术团队在端智能方面不断探索，特别地，在运动健康场景下实现了实践落地和业务赋能，这就是AI运动项目。AI运动项目践行运动数字化的理念，为运动人口的上翻提供了重要支撑，迈出了阿里体育端智能运动领域的第一步，为用户带来了更加有趣的新颖玩法。上线以来，项目受到了广泛关注。</p>
<p>2020年因新冠疫情，传统的线下运动受到限制，居家运动逐渐成为新趋势。基于阿里巴巴强大的技术沉淀，阿里体育团队顺应线上运动的迫切需要，开发出基于AI识别的智能运动，为用户提供了简便、好玩的新型居家运动方式。只需一部手机和3-4平米的场地，就可以开展AI运动。运动时，用户打开乐动力APP，将手机固定在场地一侧，适当设置手机角度，根据应用的自动语音提示调整身体与手机距离，直到人体完全位于识别框内，即可开始运动。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/badf5bd1721048c3b9261518aa025460~tplv-k3u1fbpfcp-zoom-1.image" alt="1.gif" title="1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">二 端智能实践</h3>
<p>经过⼀年的探索和完善，从验证DEMO到囊括多种动作、支持能力迁移的AI运动智能平台，阿⾥体育建立了系统化的客户端运动智能体系。端智能运动体系基于阿里深度推理引擎在手机端进行推理，识别⼈体姿态和动作，分析人体姿态、运动轨迹、动作角度等，给出实时反馈并进行动作纠正，通过能力的模块化组合，现已支持十多种运动动作和数十种玩法，实现了运动与AI的有机整合，让用户的线上运动变得上手简单而又充满趣味。</p>
<h3 data-id="heading-2">三 技术支持</h3>
<p>端智能运动的基本技术思路是运用MNN推理引擎进行推理和姿态识别。即</p>
<ul>
<li>实时检测图像及视频中的人体轮廓，定位人体14个关键骨骼点，包括头、肩、脚等重点关节部位。</li>
<li>基于这些关键点信息，连点成线、连线形成动作，可以分析人体姿态、动作角度和运动轨迹。</li>
<li>通过动作姿态匹配，检测用户运动动作，实现动作的计时与计数。同时，实时检测分析动作标准化程度，给出状态反馈，纠正用户动作，实现互动，提高交互体验。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b4e6b01ae7e40e8b2d95e005051d9c8~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>传统运动方式下，用户在运动时可以及时得到现场辅助人员（教练员、考官或亲友）的实时提醒和帮助。端智能运动方式下，用户在做动作时只能与手机应用进行交互。交互的能力和识别水平会受到推理模型能力、运动场景复杂度、运动匹配识别算法等一系列因素的影响。在端智能运动能力的探索和落地过程中，会遇到一些新的问题或者难题，如人机方位匹配、骨骼点识别丢点、点误识别、二维失真、用户移动、手机晃动、场景噪声等。这些问题不一一赘述，仅选取几个有代表性的问题进行分享：</p>
<ul>
<li>动作的有效性判断及关键算法设计，以提高动作匹配精度，这是智能运动能力的基础。</li>
<li>在保证识别效果的前提下，采取有效措施，降低移动终端的资源消耗，以提升用户体验，主要表现是费电和发热。</li>
<li>采取更加灵活的方式，减轻移动端测试的人力和时间消耗，提高开发和测试效率，为团队的交付保障提供有力支撑。</li>
</ul>
<p><strong>提升识别精度</strong></p>
<p>智能运动带给用户的最直观、最基础的感受就是动作计数准确性。如果动作识别计数不准，用户使用APP的积极性就会打消，参与性就不高。为此，我们要首先解决计数准不准的问题。</p>
<p>智能运动计数的基本原理是，把一个完整动作分解成若干个小步骤，然后对每个步骤触发识别和判断，全部步骤遍历后，对整个动作进行有效性确认。如果有效，计数加1；反之就重复上述过程。简言之，智能运动识别与计数是一个状态机。将一个运动动作离散化，抽象成N个状态机，&#123;s(0),s(1),s(2),...,s(n-1)&#125;，状态机按照一定的顺序依次进行检测，全部检测到意味用户完成了该动作，对计数加1；若某个状态未被检测到，触发对应反馈信息，重置状态机进入新的循环。每一个状态机对应着一定的触发条件，通过实时骨骼点坐标与状态的循环匹配性检测，获取一个动作匹配结果。</p>
<p>不难看出，动作识别精度与动作匹配算法紧密相关，算法匹配效果好，识别精度就越高。为提高动作识别精度，可以选取影响匹配算法的因素作为切入点和突破口，骨骼点、状态机、匹配等。相应的解决办法为：</p>
<ul>
<li>提高骨骼点稳定性，确保状态匹配结果精度。</li>
<li>选择骨骼点稳定、易识别、具有代表性的动作作为状态机。</li>
<li>帧率要能够覆盖一个动作的所有状态机。</li>
</ul>
<p>下面将举例进行说明。</p>
<p>骨骼点识别准确度对动作匹配有着重要影响。如下图所示：测试对象左手臂骨骼点识别出现错误。如果径直进行匹配，显然会得到错误的结果。针对这种情况，应当利用好用户的历史动作信息，在动作匹配算法上对动作匹配进行纠正。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c130c956c58490f8dad756f08a8cc64~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>还有一种情况，用户已经完成某种动作的全部动作，如下图中的开合跳，由于采样帧率低，无法捕获和识别全部开合跳运动过程中的全部姿态，造成某个状态匹配不成功，最终导致开合跳动作匹配错误。对于低帧率问题，可从模型和输入源两个方面着手。对于模型来说，在不影响动作识别精度情况下，采用精简模型，减少推理耗时。对不同的终端设备，采用不同分辨率的输入源，降低原始数据处理操作耗时。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c93ef8888f44649b5aa68cea12c1a2a~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>降低性能消耗</strong></p>
<p>受物理条件影响，手机端算力和存储空间有限。此外，深度学习推理本身包含大量的运算，资源消耗大。如果直接在端上进行深度学习推理，再考虑上手机端自身业务（如摄像头、录制视频、动画效果）的资源消耗，CPU和内存开销就显著增长，直观表现是手机发热明显，电量消耗很快。智能运动在端智能上落地时，要特别考虑降低性能消耗，这对于提升用户体验来说至关重要。</p>
<p>降低整体性能消耗，要追根溯源，从降低单帧消耗处着手。单帧处理可以划分为三个阶段：分别是推理前、推理和推理后。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5c192ad92e44c7b9c3aea5fa37ed409~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这三个阶段分别起着不同的作用。推理前阶段主要完成格式转换，将摄像头获取的流数据转换为推理需要的数据格式，如YUV格式、RGBA格式。推理阶段主要完成计算输出骨骼点坐标。对输入的帧数据，经过推理引擎，执行一系列算法，输出推理结果，如姿态识别是将输入图片的RGBA数据转换成骨骼点坐标数据。推理后阶段主要完成展示，进行渲染操作和业务相关操作，如UI展示、动画效果展示。</p>
<p>相应地，可对上述三个阶段分别进行优化。其中，推理过程中的优化由阿里深度推理引擎MNN负责，这里不作讨论。对于推理前阶段的数据转换，应减少不必要的中间转换环节，直接将摄像头流数据转换成为需要的格式。如推理使用RGBA裸数据，就直接将摄像头流数据转换为RGBA格式。对于推理后阶段，应根据承载的平台选择合适的渲染方案，降低渲染消耗。对于iOS平台，可直接采用Metal进行渲染提效。</p>
<p><strong>提高测试效率</strong></p>
<p>AI智能运动是阿里体育团队在体育数字化上的一次大胆尝试。在应用开发特别是测试环节中，投入相当的人力、设备及时间，不断完善应用功能、优化应用性能、提升用户体验。此外，AI运动识别的效果测试受环境因素的影响较大，如光线、背景、距离、人物在摄像头中的成像大小等。这就对测试方式提出了考验。</p>
<p>以传统测试方案为例：一般是真人、实地、实时动作，测试人员手动记录结果再事后分析，如下图所示。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/deb8a854b19d43279983cb2d8c43a55f~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不难想象，AI智能运动所运行的手机有着不同的品牌、型号、系统版本和性能参数，AI智能运动的用户可能处于不同的使用环境，若采用传统的测试方式，对不同因素进行测试覆盖，对测试人员、测试时间提出了很大的挑战，测试的一致性与精度也难以保证。具体原因如下：</p>
<ul>
<li>人工成本较高：一次测试需多名同学配合，耗时耗力。</li>
<li>测试环境较单一：无法应对线上复杂多样的环境。</li>
<li>测试结果量化难。无法对模型的精度、算法的效率、动动匹配准确度、精度提升度、性能消耗等量化评估。</li>
<li>问题定位难。事后分析排查，无法复现定位线上客诉问题。</li>
</ul>
<p>传统的测试方法难以为继，为克服上述困难，阿里体育技术团队开发了一套AI运动自动测试工具，专门用于解决AI智能项目测试难题，实现了线上问题的快捷定位与回归，并对模型算法精度实现量化评估。</p>
<p>自动测试工具的解决思路是：批量解析视频集，模拟真实场景，获取骨骼点数据，进行业务结果测试，自动生成测试报告。具体技术方案如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/286e0c41c84b47ce9f29ac8df27b93b1~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>采用新的测试工具后，显著地降低了人工成本、提高了测试效率。具体测试效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1a6e8b355b84ac38d46372c2384282d~tplv-k3u1fbpfcp-zoom-1.image" alt="2.gif" title="2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24550e82dac84eeaaa0a4b51f848a2bd~tplv-k3u1fbpfcp-zoom-1.image" alt="3.gif" title="3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>需要注意的是，测试工具的效果与测试样本的数量相关，样本越丰富，测试精度越好。</p>
<h3 data-id="heading-3">四 业务结果</h3>
<p>阿里体育智能运动现已支持数十种运动动作，开发出丰富的AI训练课程，同时通过运动能力的模块化组合，支持未来不断拓展新的动作。</p>
<p>自AI智能运动诞生以来，乐动力APP陆续上线了直臂开合跳、俯卧撑等上肢动作，臀桥、深蹲等下肢动作以及跳绳、开合跳等全身动作等多种运动形式，使得用户可以不受时间和场地限制，随时随地和朋友一起参与到AI运动，提升了APP的用户吸引力和趣味性。此外，AI训练课程创新引进明星资源，推进全年52周每周7天不间断的“明星陪练”课，以明星带动用户养成运动习惯、快乐运动、爱上运动。阿里体育团队也将不断地根据用户需要打造更多的运动玩法，丰富产品功能，形成阿里体育端智能的独特业务品牌和创新产品特色。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9a34fc932a948ab8fffa118c0780373~tplv-k3u1fbpfcp-zoom-1.image" alt="4.gif" title="4.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc291a3714ba49918470043d93e1baa9~tplv-k3u1fbpfcp-zoom-1.image" alt="5.gif" title="5.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc424eb2c7c04e38bdd84d01d7c3ac7e~tplv-k3u1fbpfcp-zoom-1.image" alt="6.gif" title="6.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4880bf611d82408fa71e0ad0f5adcf75~tplv-k3u1fbpfcp-zoom-1.image" alt="7.gif" title="7.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fclick.aliyun.com%2Fm%2F1000284017%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://click.aliyun.com/m/1000284017/" ref="nofollow noopener noreferrer">原文链接</a></p>
<p>本文为阿里云原创内容，未经允许不得转载。</p></div>  
</div>
            