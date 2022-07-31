
---
title: 'AI 篮球裁判火了，走步算得特别准，就问哈登慌不慌'
categories: 
 - 金融
 - 新浪财经
 - 新浪财经－国內
headimg: 'https://n.sinaimg.cn/spider20220731/732/w478h254/20220731/3e3d-cd90e425739b5670b9ebf38ac7f702ee.gif'
author: 新浪财经
comments: false
date: Sun, 31 Jul 2022 06:13:25 GMT
thumbnail: 'https://n.sinaimg.cn/spider20220731/732/w478h254/20220731/3e3d-cd90e425739b5670b9ebf38ac7f702ee.gif'
---

<div>   
<p>　　打篮球的友友们应该知道，走步是比赛中最常见的违规之一。</p>
<div class="img_wrapper"><img id="0" src="https://n.sinaimg.cn/spider20220731/732/w478h254/20220731/3e3d-cd90e425739b5670b9ebf38ac7f702ee.gif" alt referrerpolicy="no-referrer"><span class="img_descr"></span></div>
<p>　　为了更好地监测篮球比赛中球员是否出现走步行为，一位网名叫 @Ayush Pai 的小哥（我们就叫他 AP 哥吧）搞出了一个 AI 裁判。</p>
<div class="img_wrapper"><img id="1" src="https://n.sinaimg.cn/spider20220731/745/w480h265/20220731/a571-567e15fa96ea24d0aeb9f506d89cad48.gif" alt referrerpolicy="no-referrer"><span class="img_descr"></span></div>
<p>　　如你所见，计算机时刻“盯着”打篮球的人，并且立马能判断出这个人是否走步了。这个 AI 篮球裁判很快吸引了一批网友前来围观。有人调侃道，如果 NBA 用了该 AI 裁判，他们就完了。（因为 NBA 裁判有时候不吹走步）</p>
<div class="img_wrapper"><img id="2" src="https://n.sinaimg.cn/spider20220731/246/w786h260/20220731/d571-391f83d1123136765d7fd53d77dc15a4.png" alt referrerpolicy="no-referrer"><span class="img_descr"></span></div>
<p>　　也有人说，这个 AI 看起来对规范小孩子打篮球很有帮助。</p>
<div class="img_wrapper"><img id="3" src="https://n.sinaimg.cn/spider20220731/489/w1080h209/20220731/38bc-bbd47ddcb0b403a1ce893b336635b85e.png" alt referrerpolicy="no-referrer"><span class="img_descr"></span></div>
<p>　　还有位大聪明建议 AP 哥再设计一个奥斯卡奖的失误检测 AI。（Doge）</p>
<div class="img_wrapper"><img id="4" src="https://n.sinaimg.cn/spider20220731/204/w786h218/20220731/b9e9-2aff9219513cb36cfba709aba9e939eb.png" alt referrerpolicy="no-referrer"><span class="img_descr"></span></div>
<p>　　所以话说回来，这个 AI 裁判是怎么具备如此“火眼金睛”的呢？</p>
<p>　　你可能已经猜到了，这个 AI 裁判就是主要基于计算机视觉（CV）创造出来的。该 AI 主要跟踪两个东西：<font cms-style="strong-Bold">球的运动轨迹和人的步数。</font></p>
<p>　　为了达此目的，首先将检测运球的时间。首先，AP 哥编写了一套 CV 算法来检测球的弹跳情况，将摄像机的视图流化，即：按顺序提取视频帧。然后，AP 哥创建了一个 Aegis v 图片颜色掩码，来识别并筛选出篮球的颜色。</p>
<p>　　在计算机后台程序中，篮球显示为白色，而其其他和篮球不同色的物体都呈现为黑色；因为只有球被识别出并被放在遮罩中。</p>
<div class="img_wrapper"><img id="5" src="https://n.sinaimg.cn/spider20220731/200/w624h376/20220731/9018-9fb4deff185612375007e39ce7bc739c.gif" alt referrerpolicy="no-referrer"><span class="img_descr"></span></div>
<p>　　不过，干扰色彩导致篮球周围出现了一些不规则的像素块，为了优化这个问题，AP 哥删除了一些后处理代码，并且在球周围做了一个圆，使其看起来更规整。</p>
<div class="img_wrapper"><img id="6" src="https://n.sinaimg.cn/spider20220731/733/w1080h453/20220731/77f2-fb4fa5c7f7cd8dd3474250cbd4a90952.png" alt referrerpolicy="no-referrer"><span class="img_descr"></span></div>
<p>　　为了更好地跟踪篮球弹跳情况，AP 哥测出了其半径，根据球的半径和中心点得出的一个顶点，然后用抛物线函数来表示球的运动轨迹。当顶点达到最小值时，说明篮球触地了。</p>
<p>　　搞定篮球识别问题后，下面还要计数人在运球过程中走了几步。</p>
<p>　　AP 哥起初认为使用苹果手表上现成的步数计数器就行，不过事实证明他太天真了 —— 苹果手表上的计步器并不能实时更新。</p>
<div class="img_wrapper"><img id="7" src="https://n.sinaimg.cn/spider20220731/237/w502h535/20220731/469a-d491b98b85a4468c6026f8b0ff4bdadd.jpg" alt referrerpolicy="no-referrer"><span class="img_descr"></span></div>
<p>　　所以 AP 哥干脆自己动手，设计出一个实时计数的计步器。他创建了一个安卓应用程序，根据 x、y、z 三个轴上的加速度检测并计数步数，并将这些数据反馈给 Python 程序。</p>
<p>　　最后，<font cms-style="strong-Bold">将监测球运动轨迹和步数的两个数据集结合起来，即可判断出人是否出现走步行为。</font></p>
<p>　　不过，目前这个 AI 裁判还不够“完美”，有网友指出，这个 AI 貌似识别不到现在 NBA 里当今盛行的 gather step（哈登应该比较熟悉这个）。对此，AP 哥表示，他之后将为其加上这个功能。</p>
<div class="img_wrapper"><img id="8" src="https://n.sinaimg.cn/spider20220731/723/w1080h443/20220731/6867-249011f6173f09509a580ed7ddabb2bc.png" alt referrerpolicy="no-referrer"><span class="img_descr"></span></div>
<p>　　你是否看好这个 AI 篮球裁判？对了，AP 哥已其算法开源在 GitHub 上了，感兴趣的伙伴们可以去看看~</p>
<p>　　</p><!-- news_keyword_pub,stock, -->







<!-- 正文下iframe -->


<!-- 正文下iframe -->

<!-- 总声明-->











<!-- 总声明-->

<!-- 文末二维码 start -->


            <!-- 文末二维码 start -->
            <style>
            .appendQr_wrap&#123;border:1px solid #E6E6E6;padding:8px;&#125;
            .appendQr_normal&#123;float:left;&#125;
            .appendQr_normal img&#123;width:74px;&#125;
            .appendQr_normal_txt&#123;float:left;font-size:20px;line-height:74px;padding-left:20px;color:#333;&#125;
            </style>
            <div class="clearfix appendQr_wrap">
                <div class="appendQr_normal"><img src="https://n.sinaimg.cn/finance/cece9e13/20200514/343233024.png" referrerpolicy="no-referrer"></div>
                <div class="appendQr_normal_txt">海量资讯、精准解读，尽在新浪财经APP</div>
            </div>
            <!-- 文末二维码 start -->

            <!-- 文末二维码 start -->

<!-- 编辑姓名及工作代码 -->

<p class="article-editor">责任编辑：刘玄逸 </p>
<!-- 编辑姓名及工作代码-->

  
</div>
            