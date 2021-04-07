
---
title: 'Truora v1.1.0 发布，新增 VRF 随机数功能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6059'
author: 开源中国
comments: false
date: Wed, 07 Apr 2021 14:27:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6059'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:justify"><span style="color:#555555">随机数场景在我们的日常生活中有广泛的应用，从幼儿园入学资格、到初高中分配学校、再到买车买房买彩票，都有赖于摇号抽签。这其中，所谓的“运气”不过是随机数原理在发挥作用。</span></p> 
<p style="text-align:justify"><span style="color:#555555">如何产生公平公开的随机数是许多商业应用的核心问题。区块链作为一个多中心化的平台, 天然具有公开透明不可篡改的特性。基于区块链这些优良特性，再结合相关密码学和预言机技术，在区块链平台上产生的随机数，可实现无法预测，不可操控，且具有可验证和不可抵赖性。这对诸多应用场景都是颇具吸引力的解决方案。</span></p> 
<p style="text-align:justify"><span style="color:#555555">今年1月，微众银行开源了</span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU0MDY4MDMzOA%3D%3D%26mid%3D2247486394%26idx%3D1%26sn%3D00519c4d3b70e0b5c2b8074ad1d3b390%26chksm%3Dfb34c247cc434b51fd80a6dfac81d21892299b359a37bed187b23cfa5ba4179553ae3b31978e%26scene%3D21%23wechat_redirect" target="_blank">联盟链可信预言机解决方案Truora</a><span style="color:#555555">。</span><span style="color:#555555">此次，Truora v1.1.0发布，新增VRF随机数功能，方便开发者使用链上安全可验证随机数，助力拓宽联盟链的应用场景。</span></p> 
<p style="text-align:justify"><span style="color:#555555">在介绍VRF的原理和功能前，我们先简要回顾链上常用的随机数解决方案，并分析优缺点。</span></p> 
<p style="text-align:justify"><span style="background-color:#1e53a4; color:#1e53a4"><strong><span style="color:#1e53a4"> </span></strong></span><span style="color:#1e53a4"><strong><span style="color:#1e53a4"> 区块链随机数产生方案</span></strong></span></p> 
<p style="text-align:justify"><span style="color:#555555">通过程序生成的随机数一般都是伪随机数，伪随机数尽可能地接近其应具有的随机性，但与真随机数相比，它们由算法生成，并不是一个真实的随机过程。只要保证伪随机数的分布函数与相关性均能通过统计测试，则被认为是安全的随机数方案。伪随机数生成算法需要传入随机数种子值，简而言之，伪随机数 = 算法 + 种子。</span></p> 
<p style="text-align:justify"><strong><span style="color:#1e53a4">1、链上信息做随机数种子</span></strong></p> 
<p style="text-align:justify"><span style="color:#555555">此方案采用纯链上信息做随机数种子，如取block.number, blockhash, blocktimestamp，保证了种子的足够随机性。</span></p> 
<p style="text-align:justify"><span style="color:#555555">算法则可以采用哈希算法，如sha3,sha256,keccak256。示例代码如下：</span></p> 
<pre><code>pragma solidity <span style="color:#0e9ce5">0.4</span><span style="color:#0e9ce5">.25</span>;</code>
<code>contract Random</code><code>&#123;</code><code>   <em>// Defining a function to generate a random number</em></code><code>    function <span style="color:#dd1144">rand</span>(<span style="color:#ca7d37">uint</span> userSeed) <span style="color:#ca7d37">public</span> <span style="color:#dd1144">returns</span>(<span style="color:#ca7d37">uint</span>)&#123;</code><code>        <span style="color:#ca7d37">return</span> <span style="color:#ca7d37">uint</span>(keccak256(</code><code>        abi.encodePacked(block.timestamp, block.number, userSeed, </code><code>        block.blockhash(block.number))));</code><code>        &#125;</code><code> &#125;</code>
</pre> 
<ul> 
 <li> <p><span style="color:#555555"><strong>优点</strong>：实现简单，成本最低。</span></p> </li> 
 <li> <p><strong><span style="color:#555555">缺点</span></strong><span style="color:#555555">：</span></p> </li> 
</ul> 
<p style="text-align:justify"><span style="color:#555555">1、打包区块的节点可以一定程度上控制随机数生成。</span></p> 
<p style="text-align:justify"><span style="color:#555555">2、这种方案容易被攻击。攻击合约可以按此逻辑生成随机数，则相当于提前知道随 机数结果，然后利用此随机数结果攻击用户的业务合约。</span></p> 
<p style="text-align:justify"><strong><span style="color:#1e53a4">2、承诺-揭示</span></strong><strong><span style="color:#1e53a4">模式</span></strong></p> 
<p><span style="color:#555555">此方案是一种在规定时间内由多人参与产生随机数的流程。它的主要特点是"多人参与，两轮交互"。commit即承诺， reveal即揭示。流程如下：</span></p> 
<p><span style="color:#555555">1、在第一轮中，参与方各自生成随机数种子，并进行加密处理得到commit（如哈希处理），参与方将commit和随机数有效时间发送到链上；</span></p> 
<p><span style="color:#555555">2、在第二轮中，参与方将随机数种子明文（reveal）发到链上，合约验证commit与reveal是否匹配，并且确认随机数是在有效时间范围内；</span></p> 
<p style="text-align:justify"><span style="color:#555555">3、合约对所有reveal（随机数种子明文）进行简单运算（如求和）产生最终随机数。</span></p> 
<ul> 
 <li> <p><strong><span style="color:#555555">优点</span></strong><span style="color:#555555">：生成的随机数安全，单方无法预知，难以共谋。</span></p> </li> 
 <li> <p><strong>缺点</strong><span style="color:#555555">：</span><span style="color:#555555">多方参与，成本高。</span><span style="color:#555555">需要引入惩罚机制，交互过程中不响应，且作恶者需要被惩罚。</span></p> </li> 
</ul> 
<p style="text-align:justify"><span style="color:#1e53a4"><strong><span style="color:#1e53a4">3、通过预言机获取链下随机数</span></strong></span></p> 
<p style="text-align:justify"><span style="color:#555555">引入预言机服务，指定链下随机数网站，借助预言机获取链下随机数。</span></p> 
<p style="text-align:justify"><span style="color:#555555">例如random利用大气噪音生成真随机数并对外提供服务，可以产生实际可靠的随机数。</span><span style="color:#555555">用户可以使用预言机服务，告知此网站url，则预言机服务可以获取此网站的随机数并回写到区块链上。目前微众银行区块链开发的Truora 可信预言机解决方案已支持该功能。<span style="color:#555555">random官方网站地址如下：</span></span></p> 
<p style="text-align:justify"><span style="color:#1e53a4">https://www.random.org</span><span style="color:#555555"> </span></p> 
<ul> 
 <li> <p><strong><span style="color:#555555">优点</span></strong><span style="color:#555555">：获取链下实际可靠随机数（不是伪随机数），使用简单。</span></p> </li> 
 <li> <p><strong><span style="color:#555555">缺点</span></strong><span style="color:#555555">：需要信任预言机，预言机可以篡改结果，且随机数无法链上验证。</span></p> </li> 
</ul> 
<p style="text-align:justify"><span style="color:#555555"><span style="background-color:#1e53a4; color:#1e53a4"><strong> </strong></span><span style="color:#1e53a4"><strong> </strong></span></span><span style="color:#555555"><span style="color:#1e53a4"><strong><span style="color:#1e53a4">Truora VRF随机数方案</span></strong></span></span></p> 
<p style="text-align:justify"><span style="color:#555555">对比可知，以上三种随机数方案各有优缺点。本次微众银行区块链团队开源的VRF随机数解决方案是基于算法实现的伪随机数，需要提供随机数种子。但此方案从算法上杜绝节点或预言机单方控制随机数的生成，或篡改随机数结果。此外，VRF随机数方案具有的一个显著优点就是具有可验证性，智能合约可以验证随机数确实是用户种子和预言机私钥生成。</span></p> 
<p style="text-align:justify"><strong><span style="color:#1e53a4">1、VRF介绍</span></strong></p> 
<p style="text-align:justify"><span style="color:#555555">可验证随机函数( Verifiable Random Function ，简写 VRF )是一种将输入映射为可验证的伪随机输出的加密方案。广泛应用于区块链的共识算法和智能合约产生随机数场景中。 </span></p> 
<p style="text-align:justify"><span style="color:#555555">VRF随机数方案主要原理如下：</span></p> 
<p style="text-align:justify"><span style="color:#555555">VRF随机数的生成需要用户方和预言机服务方的两方参与。用户方提供随机数种子（seed），预言机服务方提供私钥（sk）。预言机收到用户的种子，在本地调用VRF算法生成证明（proof）和随机数结果（random），并将结果和证明传入智能合约，智能合约根据预言机服务方公钥 (pk)和用户的随机数种子 (seed)验证证明（proof）是否通过。 </span></p> 
<p style="text-align:justify"><span style="color:#555555">Truora VRF随机数方案严格按照VRF算法规范标准化文档</span><span style="color:#555555">实现，采用的是SECP256K1_SHA256_TAI加密套件。<span style="color:#555555">VRF算法规范标准化文档</span>地址如下：</span></p> 
<p style="text-align:justify"><span style="color:#1e53a4">https://tools.ietf.org/html/draft-irtf-cfrg-vrf-06#section-5</span></p> 
<p style="text-align:justify"><span style="color:#1e53a4"><strong><span style="color:#1e53a4">2、VRF使用流程</span></strong></span></p> 
<p style="text-align:justify"><span style="color:#555555">VRF使用流程跟Truora访问链下API方式类似。区别在于API方式用户需要指定url，而VRF方案需要指定随机数种子。具体使用流程如下：</span></p> 
<p><span style="color:#555555">1、用户需要继承Truora提供的抽象合约VRFClient实现自己的业务合约，我们提供了RandomNumberSampleVRF合约作为参考实现；</span></p> 
<p><span style="color:#555555">2、Truora-Service服务会监听用户的随机数种子，并且结合自己的私钥在本地调用VRF算法，生成随机数（random）和证明 (proof)。最后，Truora-Service将结果回写到VRFCore合约；</span></p> 
<p style="text-align:justify"><span style="color:#555555">3、VRFCore合约使用预言机的公钥验证随机数证明 (proof)。验证通过后，VRFCore合约将随机数回写到用户合约。</span></p> 
<p style="text-align:justify"><span style="color:#555555"><span style="background-color:#1e53a4; color:#1e53a4"><strong> </strong></span><span style="color:#1e53a4"><strong> </strong></span></span><span style="color:#555555"><span style="color:#1e53a4"><strong><span style="color:#1e53a4">相关</span></strong></span></span></p> 
<p><span style="color:#555555">此次迭代版本除了新增VRF功能外,增加了如下功能：</span></p> 
<p><span style="color:#555555">1、新增多返回值格式支持（新增string,bytes类型支持），用户可以更加灵活处理预言机 的回写结果。</span></p> 
<p><span style="color:#555555">2、新增合约版本号控制，方便用户管理不同迭代版本的合约。</span></p> 
<p style="text-align:justify"><span style="color:#555555">3、新增版本升级工具和指导文档。</span></p> 
<p style="text-align:justify"><span style="color:#555555"><span style="color:#555555"><span style="background-color:#1e53a4; color:#1e53a4"><strong> </strong></span><span style="color:#1e53a4"><strong> </strong></span></span></span><span style="color:#555555"><span style="color:#555555"><span style="color:#1e53a4"><strong><span style="color:#1e53a4">即刻体验Truora</span></strong></span></span></span></p> 
<p style="text-align:justify"><span style="color:#555555">随机数广泛应用于密码学、数值计算模拟、统计研究、游戏抽奖等场景，具有极高的商业价值。欢迎社区开发者体验VRF功能，更详细的原理和使用介绍请参看我们的文档链接: </span></p> 
<p style="text-align:justify"><span style="color:#1e53a4">https://truora.readthedocs.io/zh_CN/latest/</span> <span style="color:#1e53a4"> </span></p> 
<p style="text-align:justify"><span style="color:#555555">上述优化及功能所涉及的最新代码和技术文档已同步更新，欢迎体验和star支持。</span></p> 
<p style="text-align:justify"><span style="color:#555555"><span style="background-color:#1e53a4; color:#1e53a4"><strong> </strong></span><span style="color:#1e53a4"><strong> </strong></span></span><span style="color:#555555"><span style="color:#1e53a4"><strong>开源地址</strong></span></span></p> 
<p style="text-align:justify"><strong>github代码库地址</strong></p> 
<p style="text-align:justify"><strong><span style="color:#555555">后端代码库：</span></strong></p> 
<p><span style="color:#1e53a4">https://github.com/WeBankBlockchain/Truora-Service</span></p> 
<p style="text-align:justify"><strong><span style="color:#555555">前端代码库：</span></strong></p> 
<p style="text-align:justify"><span style="color:#1e53a4">https://github.com/WeBankBlockchain/Truora-Web</span></p> 
<p style="text-align:justify"><span style="color:#1e53a4"><strong><span style="color:#1e53a4">gitee代码库地址</span></strong></span></p> 
<p style="text-align:justify"><strong><span style="color:#555555">后端代码库: </span></strong><span style="color:#555555"> </span></p> 
<p><span style="color:#1e53a4">https://gitee.com/WeBankBlockchain/Truora-Service</span></p> 
<p style="text-align:justify"><strong><span style="color:#555555">前端代码库：</span></strong></p> 
<p style="text-align:justify"><span style="color:#1e53a4">https://gitee.com/WeBankBlockchain/Truora-Web</span></p> 
<p style="text-align:justify"><strong><span style="color:#555555">文档地址：</span></strong></p> 
<p style="text-align:justify"><span style="color:#1e53a4">https://truora.readthedocs.io/</span></p> 
<p style="text-align:justify"><strong><span style="color:#555555">首次体验Truora，可参考一键部署文档</span></strong><span style="color:#555555">：</span></p> 
<p><span style="color:#1e53a4">https://truora.readthedocs.io/zh_CN/dev/docs/Truora-Install/docker-all.html</span></p> 
<p style="text-align:justify"><strong><span style="color:#555555">如需升级已有版本，可参考</span></strong><span style="color:#555555">:</span></p> 
<p style="text-align:justify"><span style="color:#1e53a4">https://truora.readthedocs.io/zh_CN/latest/docs/upgrade.html</span></p>
                                        </div>
                                      
</div>
            