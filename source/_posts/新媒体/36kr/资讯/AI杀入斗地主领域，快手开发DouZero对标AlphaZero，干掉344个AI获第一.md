
---
title: 'AI杀入斗地主领域，快手开发DouZero对标AlphaZero，干掉344个AI获第一'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210618/v2_bc5174baafc74a488391904ed5bc91f8_img_000'
author: 36kr
comments: false
date: Fri, 18 Jun 2021 08:41:02 GMT
thumbnail: 'https://img.36krcdn.com/20210618/v2_bc5174baafc74a488391904ed5bc91f8_img_000'
---

<div>   
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/AcdhvGO-SdqODMFuVBJvUA">“量子位”（ID:QbitAI）</a>，作者：梦晨，36氪经授权发布。</p> 
<p>AlphaGo在围棋界大杀四方时就有人不服：有本事让AI斗地主试试？</p> 
<p>试试就试试。</p> 
<p><a class="project-link" data-id="30859" data-name="快手" data-logo="https://img.36krcdn.com/20200729/v2_a1a6228d3ad9447592b615f38c6bd7a3_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/30859" target="_blank">快手</a>团队开发的斗地主AI命名为DouZero，意思是像AlphaZero一样从零开始训练，不需要加入任何人类知识。</p> 
<p>只用4个GPU，短短几天的训练时间，就在Botzone排行榜上的344个斗地主AI中排名第一。</p> 
<p>而且还有在线试玩（链接在文章最后），手机也能运行。</p> 
<p>在线试玩中演示的是三人斗地主，玩家可以选择扮演地主、地主的上家或下家。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,651" src="https://img.36krcdn.com/20210618/v2_bc5174baafc74a488391904ed5bc91f8_img_000" referrerpolicy="no-referrer"></p> 
<p>选择当地主来玩玩看，可以打开显示AI手牌功能，更容<a class="project-link" data-id="46712" data-name="易观" data-logo="https://img.36krcdn.com/20200729/v2_0339d7d46d484a64a0ab6dbfde4a6628_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/46712" target="_blank">易观</a>察AI决策过程。另外可以设置AI考虑时间，默认是3秒。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,812" src="https://img.36krcdn.com/20210618/v2_f04e0754f24b4bdd81ac3b0c7a80ec0f_img_000" referrerpolicy="no-referrer"></p> 
<p>在AI的回合，会显示面临的决策和每种打法的预测胜率。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,581" src="https://img.36krcdn.com/20210618/v2_8ada7a4139ad4fc090ab845a76d92416_img_000" referrerpolicy="no-referrer"></p> 
<p>有时可以看到AI并不是简单的选择当前胜率最高的打法，而是有更全局的考虑。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,827" src="https://img.36krcdn.com/20210618/v2_41dda0f9148c43fb81471058b6cac2e7_img_000" referrerpolicy="no-referrer"></p> 
<h2>斗地主对AI来说，很难</h2> 
<p>从博弈论的角度看，斗地主是“不完全信息博弈”。</p> 
<p>围棋是所有棋子都摆在棋盘上，对弈双方都能看到的完全信息博弈。</p> 
<p>而斗地主每个玩家都看不到其他人的手牌，对于AI来说更有挑战性。</p> 
<p class="image-wrapper"><img data-img-size-val="250,305" src="https://img.36krcdn.com/20210618/v2_2ad4fcced4c043ff9b549a780f633336_img_000" referrerpolicy="no-referrer"></p> 
<p>在棋牌类游戏中，虽然斗地主的信息集的大小和数量不如麻将，但行动空间有10^4，与德州扑克相当，而大多<a class="project-link" data-id="603845" data-name="数强" data-logo="https://img.36krcdn.com/20201107/v2_6a31afda7fea46dea06967b2b127c0ac_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/603845" target="_blank">数强</a>化学习模型只能处理很小的行动空间。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,715" src="https://img.36krcdn.com/20210618/v2_049e7b1c92c84e6b8991d44bd3ea28ad_img_000" referrerpolicy="no-referrer"></p> 
<p>斗地主的所有牌型总共有27472种可能。</p> 
<p class="image-wrapper"><img data-img-size-val="468,584" src="https://img.36krcdn.com/20210618/v2_b74e8d3078ab435cb1d3c543f172b3e9_img_000" referrerpolicy="no-referrer"></p> 
<p>像下图的手牌就有391种打法。</p> 
<p class="image-wrapper"><img data-img-size-val="610,252" src="https://img.36krcdn.com/20210618/v2_3acc3d4e81774949802dbf878d992c3b_img_000" referrerpolicy="no-referrer"></p> 
<p>且斗地主的行动不容易被抽象化，使搜索的计算成本很高，像Deep Q-Learning和A3C等强化学习模型都只有不到20%的胜率。</p> 
<p>另外作为不对称游戏，几个农民要在沟通手段有限的情况下合作并与地主对抗。</p> 
<p>像扑克游戏中最流行的“反事实后悔最小化”(Counterfactual Regret Minimization)算法，就不擅长对这种竞争和合作建模。</p> 
<h2>全局、农民和地主网络并行学习</h2> 
<p>首先将手牌状态编码成4x15的独热(one-hot)矩阵，也就是15种牌每种最多能拿到4张。</p> 
<p class="image-wrapper"><img data-img-size-val="618,406" src="https://img.36krcdn.com/20210618/v2_f446f470cfd6459ebfeb363b7d1881d8_img_000" referrerpolicy="no-referrer"></p> 
<p>DouZero是在Deep Q-Learning的基础上进行改进。</p> 
<p class="image-wrapper"><img data-img-size-val="648,438" src="https://img.36krcdn.com/20210618/v2_3ac48a25493d455fbffd30316f65f64d_img_000" referrerpolicy="no-referrer"></p> 
<p>使用LSTM(长短期记忆神经网络)编码历史出牌，独热矩阵编码预测的牌局和当前手牌，最终用6层，隐藏层维度为512的MLP(多层感知机)算出Q值，得出打法。</p> 
<p>除了“学习者”全局网络以外，还用3个“角色”网络分别作为地主、地主的上家和下家进行并行学习。全局和<a class="project-link" data-id="162448" data-name="本地网" data-logo="https://img.36krcdn.com/20201111/v2_0a7aa01154ac44409ee7a91dbd7ed2df_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/162448" target="_blank">本地网</a>络之间通过共享缓冲区定期通信。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,662" src="https://img.36krcdn.com/20210618/v2_f44169ee0eb048ce92524915ab83f21d_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc">△学习者和角色的算法</p> 
<p>DouZero在48个内核和4个1080Ti的一台服务器上训练10天击败了之前的冠军，成为最强斗地主AI。</p> 
<h2>下一步，加强AI间的协作</h2> 
<p>对于之后的工作，DouZero团队提出了几个方向：</p> 
<p>一是尝试用ResNet等CNN网络来代替LSTM。</p> 
<p>以及在强化学习中尝试Off-Policy学习，将目标策略和行为策略分开以提高训练效率。</p> 
<p>最后还要明确的对农民间合作进行建模。好家伙，以后AI也会给队友倒卡布奇诺了。</p> 
<p class="image-wrapper"><img data-img-size-val="307,173" src="https://img.36krcdn.com/20210618/v2_13471fb6cb2b43eb91705465c09d83a2_img_000" referrerpolicy="no-referrer"></p> 
<p>柯洁在围棋被AlphaGO击败以后，2019年参加了斗地主锦标赛获得了冠军。</p> 
<p>不知道会不会有AI“追杀”过来继续挑战他。</p> 
<p>在线试玩：https://www.douzero.org</p> 
<p>GitHub项目地址：https://github.com/kwai/DouZero</p> 
<p>论文地址：https://arxiv.org/pdf/2106.06135.pdf</p> 
<p>参考链接：[1]https://www.sohu.com/a/285835432_498635</p>  
</div>
            