
---
title: '_PC_&nbsp;NVIDIA Research 正在開發新學習引擎 可使用基本 2D 影像建立 3D 模型'
categories: 
 - 游戏
 - 巴哈姆特
 - GNN 新聞
headimg: 'https://p2.bahamut.com.tw/B/2KU/12/dfd7c1601c2b3376957a2e08811c4vo5.JPG?v=1618803730123'
author: 巴哈姆特
comments: false
date: 2021-04-19 08:09:04
thumbnail: 'https://p2.bahamut.com.tw/B/2KU/12/dfd7c1601c2b3376957a2e08811c4vo5.JPG?v=1618803730123'
---

<div>   
<ul class="platform-tag"><li class="platform-pc"><a href="https://acg.gamer.com.tw/news.php?p=pc" target="_blank">PC 單機</a></li></ul>
<!-- 新聞內容 -->
<div>
<div>
<div>
<div>
　　NVIDIA Research 正在開發一款新學習引擎，可以使用基本的 2D 影像來建立 3D 物件模型，並且能夠在 NVIDIA Omniverse 中將影集《霹靂遊俠》裡那輛人工智慧（AI）霹靂車 KITT 這類極為經典的車輛化為現實。</div>
<div>
 </div>
<div>
<p class="caution">
【以下內容為廠商提供資料原文】</p>
</div>
</div>
<div>
 </div>
<div>
<ul class="bh-grids-img">
<li class="bh-grids-img-box" style="width: 99.74%;">
<figcaption style="padding-bottom: 46.51%"><img alt="image" name="gnnPIC" class="lazyload" data-sizes="auto" src="https://p2.bahamut.com.tw/B/2KU/12/dfd7c1601c2b3376957a2e08811c4vo5.JPG?v=1618803730123" data-srcset="https://p2.bahamut.com.tw/B/2KU/12/dfd7c1601c2b3376957a2e08811c4vo5.JPG?w=1000 1x,https://p2.bahamut.com.tw/B/2KU/12/dfd7c1601c2b3376957a2e08811c4vo5.JPG 2x" style="max-width: unset;" title referrerpolicy="no-referrer"></figcaption></li>
</ul>
</div>
<div>
 </div>
<div>
　　由位在多倫多的 NVIDIA AI Research Lab 開發的 GANverse3D 應用程式，能將平面影像打造成逼真的 3D 模型，並且可以在虛擬環境中進行視覺化的呈現和控制。這項功能可以幫助建築師、創作者、遊戲開發者和設計師輕鬆地在他們的模型中加入新的物件，無需 3D 建模方面的專業知識，也不用花費大筆預算進行渲染。</div>
<div>
 </div>
<div>
　　舉例來說，將一張汽車的照片變成一個 3D 模型，這個模型可以在虛擬場景中行駛，車上還配有逼真的頭燈、尾燈和方向燈。</div>
<div>
 </div>
<div>
<ul class="bh-grids-img">
<li class="bh-grids-img-box" style="width: 99.61%;">
<figcaption style="padding-bottom: 28.85%"><img alt="image" name="gnnPIC" class="lazyload" data-sizes="auto" src="https://p2.bahamut.com.tw/B/2KU/13/6e276edaed092171bb5a9e78641c4vp5.JPG?v=1618803737120" data-srcset="https://p2.bahamut.com.tw/B/2KU/13/6e276edaed092171bb5a9e78641c4vp5.JPG?w=1000 1x,https://p2.bahamut.com.tw/B/2KU/13/6e276edaed092171bb5a9e78641c4vp5.JPG 2x" style="max-width: unset;" title referrerpolicy="no-referrer"></figcaption></li>
</ul>
</div>
<div>
 </div>
<div>
　　為了產生訓練用的資料集，研究人員利用生成對抗網路（GAN）來合成從多個視角描繪同一物件的影像，就像攝影師圍繞一輛停放的車子走動，並從不同的角度進行拍攝。這些多視角影像被插入一個用於製作反影像的渲染框架中，這便是從 2D 影像推論出 3D 網格模型的過程。</div>
<div>
 </div>
<div>
　　使用多視角影像進行訓練後，GANverse3D 只需要一張 2D 影像便能預測出一個 3D 網格模型。此模型可以搭配 3D 神經網路渲染器，讓開發人員可以控制自訂物件和背景交換。</div>
<div>
 </div>
<div>
　　如果將 GANverse3D 當作 NVIDIA Omniverse 平台的擴充項目進行匯入，並且在 NVIDIA RTX GPU 上運行，便能透過 GANverse3D 把任何 2D 影像重新打造成 3D 物件，例如將 1980 年代熱門電影影集《霹靂遊俠》中，那輛深受觀眾喜愛、協助主角打擊犯罪的經典汽車 KITT。</div>
<div>
 </div>
<div>
　　過去用於製作反影像的模型將 3D 形狀作為訓練資料。</div>
<div>
 </div>
<div>
　　NVIDIA 研究科學家、同時也是這項研究的主要發起人 Wenzheng Chen 表示：「現在無需使用 3D 資產，我們便能將一個 GAN 模型變成一個超高效率的資料生成器，如此一來就能使用網路上的任何 2D 影像來建立 3D 物件。」</div>
<div>
 </div>
<div>
　　NVIDIA 研究人員且同為這項研究的發起人 Jun Gao 表示：「由於我們訓練使用的是真實影像，而非依賴合成資料的一般訓練管道，因此，所打造出來的人工智慧模型更適用於實際的應用程式。」</div>
<div>
 </div>
<div>
　　NVIDIA 將在接下來的兩場會議上發表 GANverse3D 背後的研究成果，分別為五月的國際學習表徵會議（International Conference on Learning Representations; ICLR）與六月的國際電腦視覺與模式識別會議（Conference on Computer Vision and Pattern Recognition; CVPR）。</div>
<div>
 </div>
<h3>
從平面影像到立體的 KITT</h3>
<div>
 </div>
<div>
　　遊戲、建築與設計領域的創作者，使用像 NVIDIA Omniverse 模擬與協作平台這樣的虛擬環境來測試新的想法，並且在打造最終產品前，以視覺化的方式呈現原型。開發人員透過 Omniverse Connectors，便能在 Omniverse 中使用他們喜愛的 3D 應用程式，以即時光線追蹤技術來模擬複雜的虛擬世界。</div>
<div>
 </div>
<div>
　　不是每個創作者都有足夠的時間和資源為他們繪製的每個物體建立 3D 模型。渲染一台展示間裡的汽車或街道上的建築物，所需捕捉的多視角影像成本可能會令人望之卻步。</div>
<div>
 </div>
<div>
　　這正是經過訓練的 GANverse3D 應用程式可以派上用場的地方，將一輛汽車、一棟建築物，甚至一匹馬的標準影像，變成可以在 Omniverse 中進行自訂及製作動畫的 3D 物件。</div>
<div>
 </div>
<div>
　　研究人員為了重建霹靂車 KITT，將汽車影像丟進訓練好的模型，讓 GANverse3D 預測出相應的 3D 紋理網格，還有車輪和頭燈等各種車輛零件。他們接著使用 NVIDIA Omniverse Kit 和 NVIDIA PhysX 工具，將預測出的紋理變成高品質的材料，讓霹靂車 KITT 的外觀和感受更加真實，並將其置於動態的駕駛序列中。</div>
<div>
 </div>
<div>
　　NVIDIA 深度學習工程師 Jean-Francois Lafleche 表示：「Omniverse 讓研究人員可以將令人興奮的先進研究成果，直接帶給創作者和終端用戶。在 Omniverse 中提供 GANverse3D 擴充項目，藝術家們將能為遊戲開發、城市規劃，甚至是訓練新的機器學習模型，創造更豐富的虛擬世界。」</div>
<div>
 </div>
<h3>
GAN 推動維度轉變</h3>
<div>
 </div>
<div>
　　從不同角度捕捉同一物體的實體資料集實屬罕見，通常是使用 ShapeNet 等合成 3D 資料集來訓練大多數將影像從 2D 轉成 3D 的 AI 工具。</div>
<div>
 </div>
<div>
　　為了從網路上的公開汽車影像等實體資料獲得多視角影像，NVIDIA 的研究人員改為使用 GAN 模型，在神經網路層進行操作，將其變成一個資料生成器。</div>
<div>
 </div>
<div>
　　研究團隊發現打開神經網路的前四層與凍結剩下的十二層，會使得 GAN 從不同視角渲染同一物體的影像。</div>
<div>
 </div>
<div>
　　凍結前四層和變動其它的十二層，神經網路會從同一個視角產生不同影像。研究人員手動分配標準視角，在特定高度和相機距離下拍攝車輛，便能從單個 2D 影像中快速產生出多視角資料集。</div>
<div>
 </div>
<div>
　　最終使用 GAN 所產生出的 55,000 張汽車影像而訓練出的模型，表現優於使用熱門 Pascal3D 資料集所訓練出的反影像網路。</div>
</div><p style="font-size: 12px; padding: 10px 0;"></p>
</div>
<!-- 新聞內容結束 -->
  
</div>
            