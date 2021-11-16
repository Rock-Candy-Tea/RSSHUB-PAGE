
---
title: '目标检测 YOLO 篇(2)'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/8207483-9dcc52ee00c0a67b.jpg'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/8207483-9dcc52ee00c0a67b.jpg'
---

<div>   
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1200" data-height="785"><img data-original-src="//upload-images.jianshu.io/upload_images/8207483-9dcc52ee00c0a67b.jpg" data-original-width="1200" data-original-height="785" data-original-format="image/jpeg" data-original-filesize="356908" src="https://upload-images.jianshu.io/upload_images/8207483-9dcc52ee00c0a67b.jpg" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">machine_learning.jpg</div>
</div>
<p>我们先来计划一下分享内容，接下来我们分享就进入了边读源码边分析过程，大概就是这个计划，今天我们来分享<strong>网络模型</strong>，先说原理然后通过代码把网络结构实现</p>
<ul>
<li>网络模型</li>
<li>数据采集</li>
<li>损失函数</li>
<li>训练模型</li>
<li>预测</li>
</ul>
<h3>YOLOv3</h3>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="638" data-height="359"><img data-original-src="//upload-images.jianshu.io/upload_images/8207483-8a8a3839447f689d.jpg" data-original-width="638" data-original-height="359" data-original-format="image/jpeg" data-original-filesize="43858" src="https://upload-images.jianshu.io/upload_images/8207483-8a8a3839447f689d.jpg" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">图</div>
</div>
<p>我们对图片分别按 <img class="math-inline" src="https://math.jianshu.com/math?formula=13%20%5Ctimes%2013" alt="13 \times 13" mathimg="1" referrerpolicy="no-referrer">、<img class="math-inline" src="https://math.jianshu.com/math?formula=26%20%5Ctimes%2026" alt="26 \times 26" mathimg="1" referrerpolicy="no-referrer"> 和 <img class="math-inline" src="https://math.jianshu.com/math?formula=52%20%5Ctimes%2052" alt="52 \times 52" mathimg="1" referrerpolicy="no-referrer"> 进行分割得到图片网格，这样做好处是我们使用不同尺寸网格来实现对图像不同大小物体都可以进行目标检测，不会丢掉小的物体，例如 <img class="math-inline" src="https://math.jianshu.com/math?formula=52%20%5Ctimes%2052" alt="52 \times 52" mathimg="1" referrerpolicy="no-referrer"> 的网格能够识别更多物体，而且物体的体积可以更小。所以我们用 <img class="math-inline" src="https://math.jianshu.com/math?formula=13%20%5Ctimes%2013" alt="13 \times 13" mathimg="1" referrerpolicy="no-referrer">、<img class="math-inline" src="https://math.jianshu.com/math?formula=26%20%5Ctimes%2026" alt="26 \times 26" mathimg="1" referrerpolicy="no-referrer"> 和 <img class="math-inline" src="https://math.jianshu.com/math?formula=52%20%5Ctimes%2052" alt="52 \times 52" mathimg="1" referrerpolicy="no-referrer"> 网格分别识别大、中和小物体。 这样做避免小物体在多次卷积之后物体信息丢失。每个网格点负责其右下角物体检测。<br>
<strong>如果物体的中心点落在某一个网格中，那么该网格就具有该物体位置和种类信息。</strong> 这句话很重要，希望大家能够理解。</p>
<h3>YOLOv3 实现</h3>
<p>我们重点就是分享 YOLOv3 是如何实现目标检测，我们根据 YOLOv3 模型结构图，一步一步来分析 YOLOv3 的目标检测算法。这是一个非常优秀的目标检测算法。为什么说优秀呢，一方面是因为 YOLOv3 表现优秀，而且算法结构还不是那么复杂。</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="848" data-height="642"><img data-original-src="//upload-images.jianshu.io/upload_images/8207483-18e2384c5b201af9.png" data-original-width="848" data-original-height="642" data-original-format="image/png" data-original-filesize="183840" src="https://upload-images.jianshu.io/upload_images/8207483-18e2384c5b201af9.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">图</div>
</div><br>
<p>只有大家将这张图吃透，随后才能够轻松地用代码来将其一步一步实现，不然就是只能大概读懂源码，至于每一块为什么要这样做，还是 consufing。</p>

<h4>主干网络</h4>
<p>左边的部分是 YOLOv3 算法的主干特征提取网络，其功能就是提取特征。</p>
<ul>
<li>输入(Input) 是 <img class="math-inline" src="https://math.jianshu.com/math?formula=416%20%5Ctimes%20416%20%5Ctimes%203" alt="416 \times 416 \times 3" mathimg="1" referrerpolicy="no-referrer"> 的图片</li>
<li>接下就是一系列特征提取过程，也就是一系列卷积的过程。在卷积过程图片高和宽不断地被压缩，而通道不断扩张，这也就是下采样的过程。通过卷积我们就得到反映的图片一系列特征层。</li>
</ul>
<h3>预测网络</h3>
<ul>
<li>我们截取最后 3 个特征层，分别是
<ul>
<li>
<img class="math-inline" src="https://math.jianshu.com/math?formula=13%20%5Ctimes%2013%20%5Ctimes%201024" alt="13 \times 13 \times 1024" mathimg="1" referrerpolicy="no-referrer">: 进行 5 次卷积，完成 5 次卷积后分两个方向进行前进，一个是现实为黄色块也就是对图片进行分类预测和回归预测。其实就是进行两次卷积得到<img class="math-inline" src="https://math.jianshu.com/math?formula=13%20%5Ctimes%2013%20%5Ctimes%2075" alt="13 \times 13 \times 75" mathimg="1" referrerpolicy="no-referrer"> ,我们输出进行分解为 <img class="math-inline" src="https://math.jianshu.com/math?formula=13%20%5Ctimes%2013%20%5Ctimes%203%20%5Ctimes%20(20%20%2B%201%20%2B%204)" alt="13 \times 13 \times 3 \times (20 + 1 + 4)" mathimg="1" referrerpolicy="no-referrer">。然后我们来一个一个看这些数字都代表什么，<img class="math-inline" src="https://math.jianshu.com/math?formula=13%20%5Ctimes%2013" alt="13 \times 13" mathimg="1" referrerpolicy="no-referrer"> 表示将图片划分为 <img class="math-inline" src="https://math.jianshu.com/math?formula=13%20%5Ctimes%2013" alt="13 \times 13" mathimg="1" referrerpolicy="no-referrer"> 个网格，然后每一个网格上存在 3 个先验框，这些先验框就是我们预先标记在图片上，然后判断这些先验框是否包含物体，如果包含物体我们就判断这些物体种类。还需要对先验框的中心进行调整将其调整到正确位置上。那么 20，1 和 4 有分别代表什么 1 代表先验框置信度也就是表示先验框中是否有物体，4 表示先验框的位置，20 是因为我们使用 VOC 数据集有 20 种类的数据集，这个可以根据自己的数据集而定。<br>
然后这个特征层还有一个去处就是对特征层进行进行上采样(也就是增加图片尺寸缩减通道数的过程)然后和 <img class="math-inline" src="https://math.jianshu.com/math?formula=26%20%5Ctimes%2026%20%5Ctimes%20512" alt="26 \times 26 \times 512" mathimg="1" referrerpolicy="no-referrer">进行堆叠，所谓堆叠就是将他们通道维度上进行合并。这样就是将<img class="math-inline" src="https://math.jianshu.com/math?formula=52%20%5Ctimes%2052%20%5Ctimes%20256" alt="52 \times 52 \times 256" mathimg="1" referrerpolicy="no-referrer">再次利用用于在 <img class="math-inline" src="https://math.jianshu.com/math?formula=26%20%5Ctimes%2026" alt="26 \times 26" mathimg="1" referrerpolicy="no-referrer"> 网格上提取特征过程。</li>
<li>
<img class="math-inline" src="https://math.jianshu.com/math?formula=26%20%5Ctimes%2026%20%5Ctimes%20512" alt="26 \times 26 \times 512" mathimg="1" referrerpolicy="no-referrer"><br>
和  <img class="math-inline" src="https://math.jianshu.com/math?formula=52%20%5Ctimes%2052%20%5Ctimes%20256" alt="52 \times 52 \times 256" mathimg="1" referrerpolicy="no-referrer"> 堆叠后也需要进行 5 次卷积。得到<img class="math-inline" src="https://math.jianshu.com/math?formula=26%20%5Ctimes%2026%20%5Ctimes%2075" alt="26 \times 26 \times 75" mathimg="1" referrerpolicy="no-referrer"> 过程和上面类似，这里不做过多的赘述了。然后同样这个特征也会通过一次上采样后和 <img class="math-inline" src="https://math.jianshu.com/math?formula=13%20%5Ctimes%2013%20%5Ctimes%201024" alt="13 \times 13 \times 1024" mathimg="1" referrerpolicy="no-referrer">
</li>
<li><img class="math-inline" src="https://math.jianshu.com/math?formula=52%20%5Ctimes%2052%20%5Ctimes%20256" alt="52 \times 52 \times 256" mathimg="1" referrerpolicy="no-referrer"></li>
</ul>
</li>
</ul>
<h3>实现主体网络</h3>
<pre><code class="python">from keras.models import Model
from keras.layers import Input

model_input = Input(shape(416,416,3))

model = Modle(model_input,model_output)
</code></pre>
<ul>
<li>输入是 <img class="math-inline" src="https://math.jianshu.com/math?formula=(416%20%5Ctimes%20416)" alt="(416 \times 416)" mathimg="1" referrerpolicy="no-referrer"> 的图片</li>
<li>输出两个表示不同大小(维度)的数组</li>
</ul>
<pre><code class="python">model_input = Input(shape(416,416,3))
model_output = body(model_input)
model = Modle(model_input,model_output)
</code></pre>
<p>接下来工作就是搭建 yolov3 的主题网络，也称称为 backbone 网络，用于提取不同尺寸大小的特征图，Darknet53.要写好代码我们就需要熟悉 yolo 网络结构，然后按照结构图一层一层的实现</p>
<pre><code class="python">def body(inputs,num_anchors,num_classes):
</code></pre>
<p>我们都已经知道主体网络用于提取特征，body 方法用于构建主体网络，接收 3 个参数分别</p>
<ul>
<li>
<strong>inputs</strong>: 输入，通常是一张<img class="math-inline" src="https://math.jianshu.com/math?formula=416%20%5Ctimes%20416%20%5Ctimes%203" alt="416 \times 416 \times 3" mathimg="1" referrerpolicy="no-referrer"> 的图片</li>
<li>
<strong>num_anchors</strong>: 每一个网格生成的多少个预选框</li>
<li>
<strong>num_classes</strong>: 表示分类种类数量</li>
</ul>
<pre><code class="python">return [y1,y2,y3]
</code></pre>
<p>那么输出就是 3 种不同尺寸的<br>
</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="278" data-height="412"><img data-original-src="//upload-images.jianshu.io/upload_images/8207483-2f2200f697788d11.jpeg" data-original-width="278" data-original-height="412" data-original-format="image/jpeg" data-original-filesize="28375" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">图</div>
</div><br>
我们对照图来一层一层写代码来实现设计图中的层或块，其实我们实现深度学习算法通常做法是打开一个设计好网络结构图，然后对照图一行一行地实现。图中的乘 1 ，乘 2 表示该块重复次数，<p></p>
<table>
<thead>
<tr>
<th>块名称</th>
<th>数量</th>
<th>filters</th>
<th>size</th>
<th>output</th>
</tr>
</thead>
<tbody>
<tr>
<td>CBL</td>
<td>1</td>
<td>32</td>
<td><img class="math-inline" src="https://math.jianshu.com/math?formula=3%20%5Ctimes%203" alt="3 \times 3" mathimg="1" referrerpolicy="no-referrer"></td>
<td><img class="math-inline" src="https://math.jianshu.com/math?formula=416%20%5Ctimes%20416%20%5Ctimes%2032" alt="416 \times 416 \times 32" mathimg="1" referrerpolicy="no-referrer"></td>
</tr>
<tr>
<td>PCBL</td>
<td>1</td>
<td>32</td>
<td><img class="math-inline" src="https://math.jianshu.com/math?formula=3%20%5Ctimes%203%2F2" alt="3 \times 3/2" mathimg="1" referrerpolicy="no-referrer"></td>
<td><img class="math-inline" src="https://math.jianshu.com/math?formula=208%20%5Ctimes%20208%20%5Ctimes%2064" alt="208 \times 208 \times 64" mathimg="1" referrerpolicy="no-referrer"></td>
</tr>
<tr>
<td>CBLR</td>
<td>1</td>
<td>32</td>
<td><img class="math-inline" src="https://math.jianshu.com/math?formula=1%20%5Ctimes%201" alt="1 \times 1" mathimg="1" referrerpolicy="no-referrer"></td>
<td></td>
</tr>
<tr>
<td></td>
<td>1</td>
<td>64</td>
<td><img class="math-inline" src="https://math.jianshu.com/math?formula=3%20%5Ctimes%203" alt="3 \times 3" mathimg="1" referrerpolicy="no-referrer"></td>
<td><img class="math-inline" src="https://math.jianshu.com/math?formula=208%20%5Ctimes%20208%20%5Ctimes%2064" alt="208 \times 208 \times 64" mathimg="1" referrerpolicy="no-referrer"></td>
</tr>
<tr>
<td>PCBL</td>
<td>1</td>
<td>128</td>
<td><img class="math-inline" src="https://math.jianshu.com/math?formula=3%20%5Ctimes%203%2F2" alt="3 \times 3/2" mathimg="1" referrerpolicy="no-referrer"></td>
<td><img class="math-inline" src="https://math.jianshu.com/math?formula=104%20%5Ctimes%20104%20%5Ctimes%20128" alt="104 \times 104 \times 128" mathimg="1" referrerpolicy="no-referrer"></td>
</tr>
<tr>
<td>CBLR</td>
<td>1</td>
<td>64</td>
<td><img class="math-inline" src="https://math.jianshu.com/math?formula=1%20%5Ctimes%201" alt="1 \times 1" mathimg="1" referrerpolicy="no-referrer"></td>
<td></td>
</tr>
<tr>
<td></td>
<td>8</td>
<td>256</td>
<td><img class="math-inline" src="https://math.jianshu.com/math?formula=3%20%5Ctimes%203" alt="3 \times 3" mathimg="1" referrerpolicy="no-referrer"></td>
<td><img class="math-inline" src="https://math.jianshu.com/math?formula=104%20%5Ctimes%20104%20%5Ctimes%20128" alt="104 \times 104 \times 128" mathimg="1" referrerpolicy="no-referrer"></td>
</tr>
<tr>
<td>PCBL</td>
<td>1</td>
<td>256</td>
<td><img class="math-inline" src="https://math.jianshu.com/math?formula=3%20%5Ctimes%203%2F2" alt="3 \times 3/2" mathimg="1" referrerpolicy="no-referrer"></td>
<td><img class="math-inline" src="https://math.jianshu.com/math?formula=52%20%5Ctimes%2052%20%5Ctimes%20256" alt="52 \times 52 \times 256" mathimg="1" referrerpolicy="no-referrer"></td>
</tr>
<tr>
<td>CBLR</td>
<td>1</td>
<td>128</td>
<td><img class="math-inline" src="https://math.jianshu.com/math?formula=1%20%5Ctimes%201" alt="1 \times 1" mathimg="1" referrerpolicy="no-referrer"></td>
<td></td>
</tr>
<tr>
<td></td>
<td>8</td>
<td>256</td>
<td><img class="math-inline" src="https://math.jianshu.com/math?formula=3%20%5Ctimes%203" alt="3 \times 3" mathimg="1" referrerpolicy="no-referrer"></td>
<td><img class="math-inline" src="https://math.jianshu.com/math?formula=52%20%5Ctimes%2052%20%5Ctimes%20256" alt="52 \times 52 \times 256" mathimg="1" referrerpolicy="no-referrer"></td>
</tr>
<tr>
<td>PCBL</td>
<td>1</td>
<td>512</td>
<td><img class="math-inline" src="https://math.jianshu.com/math?formula=3%20%5Ctimes%203%2F2" alt="3 \times 3/2" mathimg="1" referrerpolicy="no-referrer"></td>
<td><img class="math-inline" src="https://math.jianshu.com/math?formula=26%20%5Ctimes%2026%20%5Ctimes%20512" alt="26 \times 26 \times 512" mathimg="1" referrerpolicy="no-referrer"></td>
</tr>
<tr>
<td>CBLR</td>
<td>1</td>
<td>256</td>
<td><img class="math-inline" src="https://math.jianshu.com/math?formula=1%20%5Ctimes%201" alt="1 \times 1" mathimg="1" referrerpolicy="no-referrer"></td>
<td></td>
</tr>
<tr>
<td></td>
<td>8</td>
<td>512</td>
<td><img class="math-inline" src="https://math.jianshu.com/math?formula=3%20%5Ctimes%203" alt="3 \times 3" mathimg="1" referrerpolicy="no-referrer"></td>
<td><img class="math-inline" src="https://math.jianshu.com/math?formula=26%20%5Ctimes%2026%20%5Ctimes%20512" alt="26 \times 26 \times 512" mathimg="1" referrerpolicy="no-referrer"></td>
</tr>
<tr>
<td>PCBL</td>
<td>1</td>
<td>1024</td>
<td><img class="math-inline" src="https://math.jianshu.com/math?formula=3%20%5Ctimes%203%2F2" alt="3 \times 3/2" mathimg="1" referrerpolicy="no-referrer"></td>
<td><img class="math-inline" src="https://math.jianshu.com/math?formula=13%20%5Ctimes%2013%20%5Ctimes%201024" alt="13 \times 13 \times 1024" mathimg="1" referrerpolicy="no-referrer"></td>
</tr>
<tr>
<td>CBLR</td>
<td>1</td>
<td>512</td>
<td><img class="math-inline" src="https://math.jianshu.com/math?formula=1%20%5Ctimes%201" alt="1 \times 1" mathimg="1" referrerpolicy="no-referrer"></td>
<td></td>
</tr>
<tr>
<td></td>
<td>4</td>
<td>1024</td>
<td><img class="math-inline" src="https://math.jianshu.com/math?formula=3%20%5Ctimes%203" alt="3 \times 3" mathimg="1" referrerpolicy="no-referrer"></td>
<td><img class="math-inline" src="https://math.jianshu.com/math?formula=13%20%5Ctimes%2013%20%5Ctimes%201024" alt="13 \times 13 \times 1024" mathimg="1" referrerpolicy="no-referrer"></td>
</tr>
</tbody>
</table>
<pre><code class="python">def body(inputs,num_anchors,num_classes):
    out = []
    x = CBL(inputs,32,(3,3))
    n = [1,2,8,8,4]
    for i in range(5):
        x = PCBL(x,2**(6+i))
        for _ in range(n[i]):
            x = CBLR(x,2**(5+i))

        if i in [2,3,4]:
            out.append(x)

</code></pre>
<p>通过 for 循环我们将重复部分提炼出来，<img class="math-inline" src="https://math.jianshu.com/math?formula=n%20%3D%20%5B1%2C2%2C8%2C8%2C4%5D" alt="n = [1,2,8,8,4]" mathimg="1" referrerpolicy="no-referrer"> 然后我们图中每一个重复块前还有一个</p>
<p>在 CBL 中使用到的卷积 conv</p>
<h3>定义卷积 conv 方法</h3>
<p>卷积用到的参数有字典参数和列表参数</p>
<ul>
<li>列表用一个星号</li>
<li>字典用两个星号</li>
</ul>
<pre><code class="python">def conv(x):
def conv(*args,**kwargs):
    new_kwargs = &#123;'kernel_regularizer':l2(5e-4)&#125;
    new_kwargs['padding'] = 'valid' if kwargs.get('strides') == (2,2) else 'same'
    new_kwargs.update(kwargs)

    return Conv2D(*args,**new_kwargs)
</code></pre>
<h3>定义 CBL 层(块)</h3>
<p>CBL 是我们网络结构的基础，也是出现最多结构，其结构包括以下部分</p>
<ul>
<li>Conv 表示卷积层</li>
<li>BN 表示归一化</li>
<li>LeakyRelu 激活函数</li>
</ul>
<pre><code class="python">def CBL(x,*args,**kwargs):
    new_kwargs =&#123; 'use_bias': False&#125;
    new_kwargs.update(kwargs)
    x = conv(*args,**new_kwargs)(x)
    x = BatchNormalization()(x)
    x = LeakyReLU(alpha=0.1)(x)
</code></pre>
<p>这里用到了 L2 正则，L2 正则是控制参数<br>
我们通过卷积的步长(stride)来决定卷积，其实这些都卷积的基础知识。我们<br>
引入依赖</p>
<pre><code class="python">from keras.regularizers import l2
from keras.layers import Conv2D
</code></pre>
<h3>定义 PCBL 块</h3>
<p>用于在完成每一个块对卷积结果进行一次下采样，功能等于一个池化层将通过 stride=(2,2) 将图片长宽缩小为原来的 <img class="math-inline" src="https://math.jianshu.com/math?formula=%5Cfrac%7B1%7D%7B2%7D" alt="\frac&#123;1&#125;&#123;2&#125;" mathimg="1" referrerpolicy="no-referrer"></p>
<pre><code class="python">def PCBL(x,num_filters):
    x = ZeroPadding2D(((1,0),(1,0)))(x)
    x = CBL(x,num_filters,(3,3),strides=(2,2))

    return x
</code></pre>
<h3>CBLR 块</h3>
<p>CBLR 就是我们在图中重复结构，显示一个 <img class="math-inline" src="https://math.jianshu.com/math?formula=1%20%5Ctimes%201" alt="1 \times 1" mathimg="1" referrerpolicy="no-referrer"> 卷积，用于对通道数减半的卷积，接下拉就是<img class="math-inline" src="https://math.jianshu.com/math?formula=3%20%5Ctimes%203" alt="3 \times 3" mathimg="1" referrerpolicy="no-referrer"> 卷积层同时将通道数翻倍。随后一个将输入和输出在通道上进行叠加通道数翻倍。</p>
<pre><code class="python">def CBLR(x,num_filters):
    y = CBL(x,num_filters,(1,1))
    y = CBL(y,num_filters*2,(3,3))
    x = Add()([x,y])

    return x
</code></pre>
<h3>检测网络</h3>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="658" data-height="448"><img data-original-src="//upload-images.jianshu.io/upload_images/8207483-111b4563ea6940c3.png" data-original-width="658" data-original-height="448" data-original-format="image/png" data-original-filesize="107417" src="https://upload-images.jianshu.io/upload_images/8207483-111b4563ea6940c3.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">屏幕快照 2020-05-24 下午3.55.08.png</div>
</div>
<p>接下来将主干网络提取特征通过处理输出我们之前提到的 3 中不同尺寸的矩阵</p>
<pre><code class="python">    x1 = CBL5(out[2],512)
    y1 = CBLC(x1,512,num_anchors*(num_classes+5))

    x = CBLU(x1,256)
    x = Concatenate()([x,out[1]])

    x2 = CBL5(x,256)
    y2 = CBLC(x2, 256, num_anchors * (num_classes + 5))

    x = CBLU(x2,128)
    x = Concatenate()([x, out[0]])

    x3 = CBL5(x,128)
    y3 = CBLC(x3, 128, num_anchors * (num_classes + 5))

    return [y1,y2,y3]
</code></pre>
<h3>CBL5 层</h3>
<p>这个解构就是</p>
<pre><code class="python">def CBL5(x,num_filters):
    x = CBL(x, num_filters, (1,1))
    x = CBL(x, num_filters*2, (3,3))
    x = CBL(x, num_filters, (1,1))
    x = CBL(x, num_filters*2, (3,3))
    x = CBL(x, num_filters, (1,1))

    return x
</code></pre>
<h3>CBLC</h3>
<pre><code class="python">def CBLC(x,num_filters,out_filters):
    x = CBL(x, num_filters * 2, (3, 3))
    x = conv(out_filters,(1,1))(x)

    return x
</code></pre>
<h3>CBLU 层</h3>
<p>在 CBL 层上添加一个上采样层，经过 CBLU 后宽度和长度翻倍便于参加网格较大尺寸的层输出。例如<img class="math-inline" src="https://math.jianshu.com/math?formula=13%20%5Ctimes%2013" alt="13 \times 13" mathimg="1" referrerpolicy="no-referrer"> 会经过 CBLU 扩大为<img class="math-inline" src="https://math.jianshu.com/math?formula=26%20%5Ctimes%2026" alt="26 \times 26" mathimg="1" referrerpolicy="no-referrer">。</p>
<pre><code class="python">def CBLU(x, num_filters):
    x = CBL(x, num_filters, (1, 1))
    x = UpSampling2D(2)(x)

    return x
</code></pre>
  
</div>
            