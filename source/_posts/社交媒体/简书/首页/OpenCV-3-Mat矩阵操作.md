
---
title: 'OpenCV-3-Mat矩阵操作'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/1801561-3bf33ff9648c4a4e.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/1801561-3bf33ff9648c4a4e.png'
---

<div>   
<h3>1 摘要</h3>
<p>上一篇文章已经介绍了矩阵类自己的方法，本章将会详细介绍和矩阵运算相关的函数。下表简单列举了列举了这些以矩阵为参数或者为返回值的函数。</p>
<table>
<thead>
<tr>
<th style="text-align:left">参数method的取值</th>
<th style="text-align:left">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left">cv::abs()</td>
<td style="text-align:left">矩阵内所有元素取绝对值并返回结果</td>
</tr>
<tr>
<td style="text-align:left">cv::absdiff()</td>
<td style="text-align:left">计算两个矩阵差值的绝对值并返回结果</td>
</tr>
<tr>
<td style="text-align:left">cv::add()</td>
<td style="text-align:left">两个矩阵逐元素相加</td>
</tr>
<tr>
<td style="text-align:left">cv::addWeighted()</td>
<td style="text-align:left">两个矩阵逐元素加权求和，可以理解为Alpha混合</td>
</tr>
<tr>
<td style="text-align:left">cv::bitwise_and()</td>
<td style="text-align:left">两个矩阵逐元素按位与运算</td>
</tr>
<tr>
<td style="text-align:left">cv::bitwise_not()</td>
<td style="text-align:left">两个矩阵逐元素按位非运算</td>
</tr>
<tr>
<td style="text-align:left">cv::bitwise_or()</td>
<td style="text-align:left">两个矩阵逐元素按位或运算</td>
</tr>
<tr>
<td style="text-align:left">cv::bitwise_xor()</td>
<td style="text-align:left">两个矩阵逐元素按位异或运算</td>
</tr>
<tr>
<td style="text-align:left">cv::calcCovarMatrix()</td>
<td style="text-align:left">计算一组n维向量的协方差</td>
</tr>
<tr>
<td style="text-align:left">cv::cartToPolar()</td>
<td style="text-align:left">计算二维向量的角度和幅度</td>
</tr>
<tr>
<td style="text-align:left">cv::checkRange()</td>
<td style="text-align:left">检查矩阵的无效值</td>
</tr>
<tr>
<td style="text-align:left">cv::compare()</td>
<td style="text-align:left">对两个矩阵中的所有元素应用一个指定的比较运算符</td>
</tr>
<tr>
<td style="text-align:left">cv::completeSymm()</td>
<td style="text-align:left">通过将一半元素复制到另一半使得矩阵对称</td>
</tr>
<tr>
<td style="text-align:left">cv::convertScaleAbs()</td>
<td style="text-align:left">缩放矩阵，取绝对值，然后将其中数据格式转化为8位无符号型</td>
</tr>
<tr>
<td style="text-align:left">cv::countNonZero()</td>
<td style="text-align:left">计算矩阵中的非零元素</td>
</tr>
<tr>
<td style="text-align:left">cv::arrToMat()</td>
<td style="text-align:left">将2.1版本之前的数组转化为cv::Mat的实例</td>
</tr>
<tr>
<td style="text-align:left">cv::dct()</td>
<td style="text-align:left">计算矩阵的离散余弦变换</td>
</tr>
<tr>
<td style="text-align:left">cv::determinant()</td>
<td style="text-align:left">计算方阵的行列式</td>
</tr>
<tr>
<td style="text-align:left">cv::dft()</td>
<td style="text-align:left">计算矩阵的离散傅立叶变换</td>
</tr>
<tr>
<td style="text-align:left">cv::divide()</td>
<td style="text-align:left">对两个矩阵执行逐元素除法运算</td>
</tr>
<tr>
<td style="text-align:left">cv::eigen()</td>
<td style="text-align:left">计算方针的特征值和特征向量</td>
</tr>
<tr>
<td style="text-align:left">cv::exp()</td>
<td style="text-align:left">对矩阵执行逐元素求指数幂运算</td>
</tr>
<tr>
<td style="text-align:left">cv::extractImageCOI()</td>
<td style="text-align:left">从2.1之前版本的数组中提取单个通道</td>
</tr>
<tr>
<td style="text-align:left">cv::flip()</td>
<td style="text-align:left">绕指定轴翻转矩阵</td>
</tr>
<tr>
<td style="text-align:left">cv::gemm()</td>
<td style="text-align:left">执行广义的矩阵乘法</td>
</tr>
<tr>
<td style="text-align:left">cv::getConvertElem()</td>
<td style="text-align:left">获取单个像素的类型转换函数</td>
</tr>
<tr>
<td style="text-align:left">cv::getConvertScaleElem()</td>
<td style="text-align:left">获取单个像素的类型转换和缩放函数</td>
</tr>
<tr>
<td style="text-align:left">cv::idct()</td>
<td style="text-align:left">计算矩阵的离散余弦逆变换</td>
</tr>
<tr>
<td style="text-align:left">cv::idft()</td>
<td style="text-align:left">计算矩阵的离散傅立叶逆变换</td>
</tr>
<tr>
<td style="text-align:left">cv::inRange()</td>
<td style="text-align:left">测试矩阵的元素是否包含在其他两个矩阵的值之间</td>
</tr>
<tr>
<td style="text-align:left">cv::invert()</td>
<td style="text-align:left">求方阵的逆</td>
</tr>
<tr>
<td style="text-align:left">cv::log()</td>
<td style="text-align:left">逐元素计算自然对数</td>
</tr>
<tr>
<td style="text-align:left">cv::magnitude()</td>
<td style="text-align:left">计算二维向量的幅度</td>
</tr>
<tr>
<td style="text-align:left">cv::LUT()</td>
<td style="text-align:left">将矩阵转换为查找表的索引</td>
</tr>
<tr>
<td style="text-align:left">cv::Mahalanobis()</td>
<td style="text-align:left">计算两个向量之间的马氏距离</td>
</tr>
<tr>
<td style="text-align:left">cv::max()</td>
<td style="text-align:left">逐元素求两个矩阵之间的最大值</td>
</tr>
<tr>
<td style="text-align:left">cv::mean()</td>
<td style="text-align:left">计算矩阵元素的平均值</td>
</tr>
<tr>
<td style="text-align:left">cv::meanStdDev()</td>
<td style="text-align:left">计算数组元素的均值和标准差</td>
</tr>
<tr>
<td style="text-align:left">cv::merge()</td>
<td style="text-align:left">将多个单通道矩阵合并为一个多通道矩阵</td>
</tr>
<tr>
<td style="text-align:left">cv::min()</td>
<td style="text-align:left">逐元素求两个矩阵之间的最小值</td>
</tr>
<tr>
<td style="text-align:left">cv::minMaxLoc()</td>
<td style="text-align:left">在矩阵中寻找最大和最小值</td>
</tr>
<tr>
<td style="text-align:left">cv::mixChannels()</td>
<td style="text-align:left">打乱从输入矩阵到输出矩阵的通道</td>
</tr>
<tr>
<td style="text-align:left">cv::mulSpectrums()</td>
<td style="text-align:left">对两个傅立叶谱矩阵执行逐元素乘法运算</td>
</tr>
<tr>
<td style="text-align:left">cv::multiply()</td>
<td style="text-align:left">对两个矩阵执行逐元素乘法运算</td>
</tr>
<tr>
<td style="text-align:left">cv::mulTransposed()</td>
<td style="text-align:left">计算矩阵和其转置对逐元素乘积</td>
</tr>
<tr>
<td style="text-align:left">cv::norm()</td>
<td style="text-align:left">在两个矩阵之间计算归一化相关系数</td>
</tr>
<tr>
<td style="text-align:left">cv::normalize()</td>
<td style="text-align:left">将矩阵中对元素标准化到某个值内</td>
</tr>
<tr>
<td style="text-align:left">cv::perspectiveTransform()</td>
<td style="text-align:left">执行一系列向量的透视矩阵变换</td>
</tr>
<tr>
<td style="text-align:left">cv::phase()</td>
<td style="text-align:left">计算二维向量的方向</td>
</tr>
<tr>
<td style="text-align:left">cv::polarToCart()</td>
<td style="text-align:left">已知角度和幅度，求二维向量</td>
</tr>
<tr>
<td style="text-align:left">cv::pow()</td>
<td style="text-align:left">对矩阵内对每个元素执行幂运算</td>
</tr>
<tr>
<td style="text-align:left">cv::randu()</td>
<td style="text-align:left">使用均匀分布的随机数填充矩阵</td>
</tr>
<tr>
<td style="text-align:left">cv::randn()</td>
<td style="text-align:left">使用正态分布的随机数填充矩阵</td>
</tr>
<tr>
<td style="text-align:left">cv::randShuffle()</td>
<td style="text-align:left">随机打乱矩阵元素</td>
</tr>
<tr>
<td style="text-align:left">cv::reduce()</td>
<td style="text-align:left">通过特定的操作将二维矩阵退化为向量</td>
</tr>
<tr>
<td style="text-align:left">cv::repeat()</td>
<td style="text-align:left">将一个矩阵的内容复制到另外一个矩阵</td>
</tr>
<tr>
<td style="text-align:left">cv::saturate_cast<>()</td>
<td style="text-align:left">饱和转换原始类型</td>
</tr>
<tr>
<td style="text-align:left">cv::scaleAdd()</td>
<td style="text-align:left">逐元素的执行矩阵加法，第一个矩阵可以选择先执行缩放操作</td>
</tr>
<tr>
<td style="text-align:left">cv::setIdentity()</td>
<td style="text-align:left">将对角线上的元素设置为1，其余元素设置为0</td>
</tr>
<tr>
<td style="text-align:left">cv::solve()</td>
<td style="text-align:left">求出线性方程组的解</td>
</tr>
<tr>
<td style="text-align:left">cv::solveCubic()</td>
<td style="text-align:left">计算三次方程的实根</td>
</tr>
<tr>
<td style="text-align:left">cv::solvePoly()</td>
<td style="text-align:left">找到多项式方程的复根</td>
</tr>
<tr>
<td style="text-align:left">cv::sort()</td>
<td style="text-align:left">排序矩阵中的任意行或者列的所有元素</td>
</tr>
<tr>
<td style="text-align:left">cv::sortIdx()</td>
<td style="text-align:left">和函数cv::sort()类似，但是这里并不会修改矩阵本身，仅返回排序结果的索引值</td>
</tr>
<tr>
<td style="text-align:left">cv::split()</td>
<td style="text-align:left">将多通道矩阵分解为多个单通道矩阵</td>
</tr>
<tr>
<td style="text-align:left">cv::sqrt()</td>
<td style="text-align:left">逐元素计算矩阵的平方根</td>
</tr>
<tr>
<td style="text-align:left">cv::subtract()</td>
<td style="text-align:left">逐元素对两个矩阵执行减法运算</td>
</tr>
<tr>
<td style="text-align:left">cv::sum()</td>
<td style="text-align:left">计算数组所有元素的和</td>
</tr>
<tr>
<td style="text-align:left">cv::theRNG()</td>
<td style="text-align:left">返回一个随机数生成器</td>
</tr>
<tr>
<td style="text-align:left">cv::trace()</td>
<td style="text-align:left">计算一个矩阵的迹</td>
</tr>
<tr>
<td style="text-align:left">cv::transform()</td>
<td style="text-align:left">对矩阵的每个元素应用矩阵变换</td>
</tr>
<tr>
<td style="text-align:left">cv::transpose()</td>
<td style="text-align:left">计算矩阵的转置矩阵</td>
</tr>
</tbody>
</table>
<p>上面所列举的函数都遵循下面列举的一些通用的规则，特殊的场景会在函数的描述中注明。</p>
<h5>饱和</h5>
<p>输出的计算结果会被饱和转换至输出矩阵的元素类型。</p>
<h5>输出</h5>
<p>如果输出矩阵的类型和尺寸不满足要求，将会使用函数<code>cv::Mat::create()</code>创建新的输出矩阵实例。通常情况下要求的输出类型和尺寸和输入矩阵相同，但是对于某些特殊的函数可能不同。如函数<code>cv::transpose</code>返回的尺寸，<code>cv::split</code>函数返回的类型会发生改变。</p>
<h5>标量</h5>
<p>大多数如<code>cv::add()</code>的计算函数都可以执行矩阵和矩阵，以及矩阵和标量的计算。矩阵和标量的矩阵计算结果和使用该标量创建一个矩阵的计算结果相同。</p>
<h5>掩码</h5>
<p>当一个函数存在掩码参数时，只有掩码元素不为0对应位置的元素才会被计算。</p>
<h5>dtype</h5>
<p>很多算法和相似的函数不会要求输入矩阵具有相同的类型，或者即使它们具有相同的类型，输出矩阵也可能是不同的类型。在这些场景下，输出矩阵必须通过参数<code>dtype</code>明确的制定它的深度。当函数或者算法中需要设置此参数时，它可以被设置为任何基础数据类型，如<code>CV_32F</code>，其规定了输出矩阵中的基本数据类型。如果输入矩阵的类型相同，该参数可以设置为默认值-1，这样输出矩阵的数据类型就会和输入矩阵保持一致。</p>
<h5>原位操作</h5>
<p>除非另有说明，任何输入矩阵和输出矩阵具有相同尺寸和类型的操作都结果直接写入到输入矩阵中。</p>
<h5>多通道</h5>
<p>对于不需要使用多通道的操作，如果存在多通道的参数，则每个通道会被单独处理。</p>
<h3>2 函数清单</h3>
<h5>cv::abs()</h5>
<p>该函数计算一个矩阵或者矩阵表达式的绝对值，最常使用的场景是计算矩阵中每个元素的绝对值，该函数的原型如下。</p>
<pre><code>cv::MatExpr cv::abs(cv::InputArray src);
// 以矩阵表达式作为参数
cv::MatExpr cv::abs(const cv::MatExpr& src); 
</code></pre>
<p>该函数在处理矩阵参数和表达式参数时能够恰当的识别和处理一些特殊场景，并转化为<code>cv::absDiff()</code>或者其他函数去处理具体的逻辑。例如在处理下列场景时内部会转化为其他函数。</p>
<pre><code>m2 = cv::abs(m0 - m1) 
会被转化为cv::absdiff(m0, m1, m2)

m2 = cv::abs(m0)
会被转化为m2 = cv::absdiff(m0, cv::Scalar::all(0), m2)

m2 = cv::Mat_<Vec<uchar,n>>(cv::abs(alpha*m0 + beta))(alpha和beta为实数)
会被转化为cv::convertScaleAbs(m0, m2, alpha, beta)
</code></pre>
<p>第三个例子是计算一个n通道矩阵的缩放和平移结果，如在校正图像对比度时可能会使用到这个表达式。在被函数<code>cv::absdiff()</code>替代的实例中，计算的结果和输入数组保持相同的大小和元素数据类型，在被函数<code>cv::convertScaleAbs()</code>替代的例子中，计算结果的元素基本数据类型总为<code>CV_U8</code>。</p>
<h5>cv::absdiff()</h5>
<p>该函数计算两个矩阵中对应元素的差值，并取其绝对值，将结果写入到指定矩阵中，其原型如下。</p>
<pre><code>// src1：被减矩阵
// src2：减矩阵
// dst：计算结果
void cv::absdiff(cv::InputArray src1, cv::InputArray src2, cv::OutputArray dst)
</code></pre>
<p>该函数会对结果进行饱和转换，计算公式如下。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="544" data-height="42"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-3bf33ff9648c4a4e.png" data-original-width="544" data-original-height="42" data-original-format="image/png" data-original-filesize="14956" src="https://upload-images.jianshu.io/upload_images/1801561-3bf33ff9648c4a4e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h5>cv::add()</h5>
<p>该函数计算两个矩阵中对应元素的和，并将结果写入到指定矩阵中，其原型如下。</p>
<pre><code>// src1：第一个矩阵
// src2：第二个矩阵
// dot：计算结果
// mask：计算掩码矩阵，可选参数，只有当掩码对应元素不为0时，该位置对应的两个输入矩阵才会计算
// dtype：输出矩阵的基本数据类型
void cv::add(cv::InputArray src1, cv::InputArray src2, cv::OutputArray dst, 
             cv::InputArray mask = cv::noArray(), int dtype = -1);
</code></pre>
<p>该函数会对结果进行饱和转换，计算公式如下。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="544" data-height="48"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-8bb62796572c5f80.png" data-original-width="544" data-original-height="48" data-original-format="image/png" data-original-filesize="16751" src="https://upload-images.jianshu.io/upload_images/1801561-8bb62796572c5f80.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>需要注意的是对于一些简单的运算可以直接使用表达式，OpenCV会调用合适的函数完成计算，如。</p>
<pre><code>// 简单矩阵加法表达式
dst = src1 + src2;
dst += src1;
</code></pre>
<h5>cv::addWeighted()</h5>
<p>该函数是对两个矩阵的加权求和，其原型如下。</p>
<pre><code>// src1: 第一个输入矩阵
// alpha: 第一个输入矩阵的权重
// src2: 第二个输入矩阵
// beta: 第二个输入矩阵的权重
// gamma: 计算结果的偏移值
// dst: 计算结果
// dtype: 输出矩阵元素的数据类型
void cv::addWeighted(cv::InputArray src1, double alpha,
                     cv::InputArray src2, double beta,
                     double gamma, cv::OutputArray dst, int dtype = -1);
</code></pre>
<p>该函数的计算公式如下。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="824" data-height="50"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-5d828ab539c7f262.png" data-original-width="824" data-original-height="50" data-original-format="image/png" data-original-filesize="23032" src="https://upload-images.jianshu.io/upload_images/1801561-5d828ab539c7f262.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>两个源矩阵只要尺寸相同，它们中的元素可以有不同的数据类型，也可以有不同的通道数，如一个是灰度图，而另一个是彩图。该函数可以实现图像透明度混合，即可以将上式中的γ设置为0，并使β+α=1，则可以得到如下公式。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="818" data-height="48"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-ee371cc36e55899e.png" data-original-width="818" data-original-height="48" data-original-format="image/png" data-original-filesize="22535" src="https://upload-images.jianshu.io/upload_images/1801561-ee371cc36e55899e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>函数<code>cv::addWeighted()</code>非常灵活，通常将参数<code>alpha</code>和<code>beta</code>设置为大于等于0的数，参数<code>gamma</code>的设置通常取决于图像像素的平均值或者最大值。下面展示了一个实现了图像透明度混合<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2FStarryThrone%2FOpenCV_Learning_Notes%2Ftree%2Fmaster%2FC3_MatOperations" target="_blank">实例</a>的部分核心代码。</p>
<pre><code>// 图像Src1的数据会被混合到图像Src2指定中
cv::Mat src = cv::imread(..., cv::IMREAD_COLOR);
cv::Mat dst = cv::imread(..., cv::IMREAD_COLOR);

// 获取在Src2中混合的起点位置
int x = ...;
int y = ...;

// 获取混合的参数
double alpha = ...;
double beta = ...;

// 混合图像
cv::Mat target = cv::Mat(dst, cv::Rect(x, y, src_w, src_h));
cv::addWeighted(src, alpha, target, beta, 0, target);
</code></pre>
<p>上面的代码读取了两张图像src1和src2，并分别从它们之重选取了部分数据进行混合，并展示混合后的图像src2，其效果如下图。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1000" data-height="978"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-55d8779323e3e1e6.png" data-original-width="1000" data-original-height="978" data-original-format="image/png" data-original-filesize="1876371" src="https://upload-images.jianshu.io/upload_images/1801561-55d8779323e3e1e6.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h5>cv::bitwise_and()</h5>
<p>该函数逐元素对两个矩阵执行位与运算，其原型如下。</p>
<pre><code>// src1: 第一个输入矩阵
// src2: 第二个输入矩阵
// dst：计算结果
// mask：计算掩码矩阵，可选参数，只有当掩码对应元素不为0时，该位置对应的两个输入矩阵才会计算
void cv::bitwise_and(cv::InputArray src1, cv::InputArray src2, cv::OutputArray dst,
                     cv::InputArray mask = cv::noArray());
</code></pre>
<p>如果不使用掩码矩阵，执行两个矩阵的位与计算可以直接使用如下表达式。</p>
<pre><code>dst = src1 & src2;
</code></pre>
<h5>cv::bitwise_not()</h5>
<p>该函数逐元素对某个矩阵执行位非运算，其原型如下。</p>
<pre><code>// src: 输入矩阵
// dst：计算结果
// mask：计算掩码矩阵，可选参数，只有当掩码对应元素不为0时，该位置对应的两个输入矩阵才会计算
void cv::bitwise_not(cv::InputArray src, cv::OutputArray dst,
                     cv::InputArray mask = cv::noArray());
</code></pre>
<p>如果不使用掩码矩阵，对一个矩阵执行逐元素的位非运算可以直接使用如下表达式。</p>
<pre><code>dst = !src1;
</code></pre>
<h5>cv::bitwise_or()</h5>
<p>该函数逐元素对两个矩阵执行位或运算，其原型如下。</p>
<pre><code>// src1: 第一个输入矩阵
// src2: 第二个输入矩阵
// dst：计算结果
// mask：计算掩码矩阵，可选参数，只有当掩码对应元素不为0时，该位置对应的两个输入矩阵才会计算
void cv::bitwise_and(cv::InputArray src1, cv::InputArray src2,
                     cv::OutputArray dst, cv::InputArray mask = cv::noArray());
</code></pre>
<p>如果不使用掩码矩阵，执行两个矩阵的位或计算可以直接使用如下表达式。</p>
<pre><code>dst = src1 | src2;
</code></pre>
<h5>cv::bitwise_xor()</h5>
<p>该函数逐元素对两个矩阵执行位异或运算，其原型如下。</p>
<pre><code>// src1: 第一个输入矩阵
// src2: 第二个输入矩阵
// dst：计算结果
// mask：计算掩码矩阵，可选参数，只有当掩码对应元素不为0时，该位置对应的两个输入矩阵才会计算
void cv::bitwise_and(cv::InputArray src1, cv::InputArray src2, cv::OutputArray dst,
                     cv::InputArray mask = cv::noArray());
</code></pre>
<p>如果不使用掩码矩阵，执行两个矩阵的位异或计算可以直接使用如下表达式。</p>
<pre><code>dst = src1 ^ src2;
</code></pre>
<h5>cv::calcCovarMatrix()</h5>
<p>对于一个由n维向量组成的矩阵，假设每个向量表示一组随机变量，每组变量的个数都为m，则这n个随机变量的协方差矩阵可以由下面两个函数求出。两组随机变量的协方差可以理解为是这两组变量在统计学上分布的相似程度，而n组变量的任意两组变量的协方差则构成了一个协方差矩阵。如果不熟悉协方差矩阵的数学概念，可以参考<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F37609917" target="_blank">协方差矩阵</a>。函数原型如下。</p>
<pre><code>// samples：n*1或者1*n的原始样本矩阵的地址
// nsamples：样本数
// covar：计算得到的协方差矩阵的引用
// mean：均值矩阵的引用
// flags：计算时采用的策略，具体见下表
// ctype：输出矩阵中元素的基本数据类型
void cv::calcCovarMatrix(const cv::Mat* samples, int nsamples, 
                         cv::Mat& covar, cv::Mat& mean,
                         int flags, int ctype = cv::F64);

// samples：n*m的原始样本矩阵
// 其他参数和上面函数含义一致
void cv::calcCovarMatrix(cv::InputArray samples, 
                         cv::Mat& covar, cv::Mat& mean,
                         int flags, int ctype = cv::F64);
</code></pre>
<p>该函数可以通过参数<code>flags</code>自定义计算策略，该参数所有可选的值及其含义如下表，除了特殊情况外可以使用与运算符启用多个标志。</p>
<table>
<thead>
<tr>
<th style="text-align:left">参数flags的取值</th>
<th style="text-align:left">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left">cv::COVAR_NORMAL</td>
<td style="text-align:left">计算均值和协方差矩阵</td>
</tr>
<tr>
<td style="text-align:left">cv::COVAR_SCRAMBLED</td>
<td style="text-align:left">使用快速PCA “scrambled”策略计算协方差矩阵</td>
</tr>
<tr>
<td style="text-align:left">cv::COVAR_USE_AVERAGE</td>
<td style="text-align:left">参数mean作为输入参数使用，不会计算均值矩阵</td>
</tr>
<tr>
<td style="text-align:left">cv::COVAR_SCALE</td>
<td style="text-align:left">缩放协方差矩阵计算结果</td>
</tr>
<tr>
<td style="text-align:left">cv::COVAR_ROWS</td>
<td style="text-align:left">将每行数据看成时一个向量，即一组随机变量</td>
</tr>
<tr>
<td style="text-align:left">cv::COVAR_COLS</td>
<td style="text-align:left">将每列数据看成时一个向量，即一组随机变量</td>
</tr>
</tbody>
</table>
<p>需要注意参数<code>flags</code>的<code>cv::COVAR_NORMAL</code>和<code>cv::COVAR_SCRAMBLED</code>选项是互斥的，在选择<code>cv::COVAR_NORMAL</code>和<code>cv::COVAR_ROWS</code>的情况下，协方差矩阵的计算公式如下。其中<code>vmn</code>表示原始样本第n行m列元素。vn表示第n个向量即第n组随机变量的均值。z是计算结果的缩放系数，当<code>cv::COVAR_SCALE</code>标记未启用时，其值为1。计算结果将会时一个n✖️n的矩阵。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="862" data-height="180"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-0905566fe9bda745.png" data-original-width="862" data-original-height="180" data-original-format="image/png" data-original-filesize="118379" src="https://upload-images.jianshu.io/upload_images/1801561-0905566fe9bda745.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>如果选择<code>cv::COVAR_SCRAMBLED</code>和<code>cv::COVAR_ROWS</code>，协方差矩阵的计算公式如下。注意在这个计算公式中，矩阵的转置运算符被放到了第一个矩阵之上，对于同样的n✖️m矩阵，计算得到的是尺寸为m✖️m协方差矩阵。在一些特定场景下，如对向量元素较长的样本数据计算快速主成分分析(PCA)时会使用这种技术，一个应用实例就是人脸识别的特征脸算法。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="900" data-height="174"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-ea8ca8e8bd503ea6.png" data-original-width="900" data-original-height="174" data-original-format="image/png" data-original-filesize="132060" src="https://upload-images.jianshu.io/upload_images/1801561-ea8ca8e8bd503ea6.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>当已知多维向量的均值向量时，参数<code>flags</code>可以选择<code>cv::COVAR_USE_AVERAGE</code>从而减少计算时间。对于n行✖️m列的输入样本矩阵而言，当设置<code>cv::COVAR_SCALE</code>时，计算的协方差矩阵会被缩放，缩放系数等于1.0/m，但是当<code>cv::COVAR_SCRAMBLED</code>被启用时，缩放系数则等于1.0/n，可以理解为1/单组随机变量个长度。</p>
<p>该函数的输入输出函数中元素的基本数据类型都应该是相同的浮点数类型，协方差矩阵的尺寸根据选择的是标准<code>cv::COVAR_NORMAL</code>还是反转<code>cv::COVAR_SCRAMBLED</code>的计算策略相应为n✖️n和m✖️m。</p>
<h5>cv::cartToPolar()</h5>
<p>该函数原型如下，它读取两个输入矩阵x和y，将其中对应的元素组成一个点Point(x, y)，并计算该点的极坐标表示，将其幅度(长度)和角度分别放在输出矩阵<code>magnitude</code>和<code>angle</code>中。参数<code>angleInDegrees</code>表示返回的角度矩阵单位，<code>ture</code>表示角度，<code>false</code>表示弧度。</p>
<pre><code>// x：第一个输入矩阵
// y：第二个输入矩阵
// magnitude：幅度矩阵
// angle：角度/弧度矩阵
// angleInDegrees：角度矩阵的单位，ture表示角度，false表示弧度
void cv::cartToPolar(cv::InputArray x, cv::InputArray y,
                     cv::OutputArray magnitude, cv::OutputArray angle,
                     bool angleInDegrees = false);
</code></pre>
<p>幅度计算公式如下。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="544" data-height="74"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-e6dc0093ab03d8c5.png" data-original-width="544" data-original-height="74" data-original-format="image/png" data-original-filesize="18617" src="https://upload-images.jianshu.io/upload_images/1801561-e6dc0093ab03d8c5.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>角度计算公式如下。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="544" data-height="68"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-f2aea64cc3c86928.png" data-original-width="544" data-original-height="68" data-original-format="image/png" data-original-filesize="20382" src="https://upload-images.jianshu.io/upload_images/1801561-f2aea64cc3c86928.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h5>cv::checkRange()</h5>
<p>该函数测试输入矩阵中的每个元素是否位于指定的范围之内，其原型如下。需要注意的是任何NaN或者inf值会直接被判定为超出指定范围。</p>
<pre><code>// src：待测试矩阵
// quiet：某个元素不在指定范围内是否抛出异常，Yes不会抛出异常，No会
// pos：用于存储第一个越界元素位置的地址
// minVal：指定范围最小值
// maxVal：指定范围最大值
// 返回值：是否所有元素都在指定范围内，所有元素都在返回true，任一个不在返回false
bool cv::checkRange(cv::InputArray src, bool quiet = true, cv::Point* pos = 0,
                    double minVal = -DBL_MAX, double maxVal =  DBL_MAX);
</code></pre>
<h5>cv::compare()</h5>
<p>该函数采用特定的运算符比较两个输入矩阵，其原型如下。输出矩阵<code>dst</code>中元素的基本数据类型为8位序列，如果符合比较条件将被设置为255，不符合将被设置为0。</p>
<pre><code>// src1：第一个输入矩阵
// src2：第二个输入矩阵
// dst：比较结果矩阵
// cmpop：比较策略，可选值见下文
bool cv::compare(cv::InputArray src1, cv::InputArray src2,
                 cv::OutputArray dst, int cmpop);
</code></pre>
<p>比较策略即参数cmpop的可选择值及其含义如下表。</p>
<table>
<thead>
<tr>
<th style="text-align:left">参数cmpop的取值</th>
<th style="text-align:left">比较运算符</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left">cv::CMP_EQ</td>
<td style="text-align:left">(src1i == src2i)</td>
</tr>
<tr>
<td style="text-align:left">cv::CMP_GT</td>
<td style="text-align:left">(src1i > src2i)</td>
</tr>
<tr>
<td style="text-align:left">cv::CMP_GE</td>
<td style="text-align:left">(src1i >= src2i)</td>
</tr>
<tr>
<td style="text-align:left">cv::CMP_LT</td>
<td style="text-align:left">(src1i < src2i)</td>
</tr>
<tr>
<td style="text-align:left">cv::CMP_LE</td>
<td style="text-align:left">(src1i <= src2i)</td>
</tr>
<tr>
<td style="text-align:left">cv::CMP_NE</td>
<td style="text-align:left">(src1i != src2i)</td>
</tr>
</tbody>
</table>
<p>另外你也可以直接使用运算符来完成相同的计算。</p>
<pre><code>dst = src1 == src2;
dst = src1 > src2;
dst = src1 >= src2;
dst = src1 < src2;
dst = src1 <= src2;
dst = src1 != src2;
</code></pre>
<h5>cv::completeSymm()</h5>
<p>该函数沿着矩阵对角线将一半元素拷贝到其对应的转置位置，从而使得整个矩阵对称，其原型如下。</p>
<pre><code>// mtx：需要处理的矩阵
// lowerToUpper：矩阵拷贝的方式，true表示将上三角拷贝至下三角，false则相反
bool cv::completeSymm(cv::InputArray mtx, bool lowerToUpper = false);
</code></pre>
<h5>cv::convertScaleAbs()</h5>
<p>该函数是一系列操作的集合，它首先缩放原始矩阵，再施加一个偏移量，再求其绝对值，之后将结果饱和转换为8位无符号字符型数据，其原型如下。</p>
<pre><code>// src：元素矩阵
// dst：输出矩阵
// alpha：缩放因子
// beta：偏移量
void cv::convertScaleAbs(cv::InputArray src, cv::OutputArray dst,
                         double alpha = 1.0, double beta  = 0.0);
</code></pre>
<p>需要注意的是，当参数<code>alpha</code>设置为1.0，或者参数<code>beta</code>设置为0。0时不需要为性能担忧，OpenCV是很智能的，它不会去执行无用的运算。另外为了通用性考量，可以使用如下方式实现同样的计算逻辑。</p>
<pre><code>for(int i = 0; i < src.rows; i++) &#123;
    for(int j = 0; j < src.cols*src.channels(); j++) &#123;
        dst.at<dst_type>(i, j) = satuarate_cast<dst_type>((double)src.at<src_type>(i, j) * alpha + beta);
    &#125;
&#125;
</code></pre>
<h5>cv::countNonZero()</h5>
<p>该函数计算矩阵中非零元素的个数，其原型如下。</p>
<pre><code>// mtx：输入矩阵
// 返回值：输入矩阵中非零元素的个数
int cv::countNonZero(cv::InputArray mtx);
</code></pre>
<h5>cv::cvarrToMat()</h5>
<p>该函数用于将OpenCV2.1版本之前的图像和矩阵类型转化为<code>cv::Mat</code>实例，默认情况下，该函数只会创建矩阵头，并不会去拷贝真正的数据段，因此在使用<code>cv::Mat</code>实例时不要释放老版本指向的数据段。参数<code>copyData</code>设置为<code>true</code>会拷贝原始的数据。该函数原型如下。</p>
<pre><code>// src：老版本的数组实例，如CvMat，IplImage或者CvMatND
// copyData：是否需要拷贝数据段内容
// allowND：是否允许尝试转换CvMatND实例
// coiMode：兴趣通道模式
// 该值为0时如果设置了兴趣通道则COI会抛出异常
// 如果为非零值，则忽略兴趣通道直接处理整个图像
cv::Mat cv::cvarrToMat(const CvArr* src, bool copyData = false,
                       bool allowND = true, int coiMode = 0);
</code></pre>
<p>该函数并不能转换所有的<code>CvMatND</code>实例，成功的关键在于矩阵是否连线，或者至少能够被表示为连续矩阵的序列。具体的将就是对于所有的i，或者在最坏情况下除一个<code>i</code>之外，<code>A.dim[i].size✖️A.dim.step[i]</code>的值都应该等于<code>A.dim.step[i-1]</code>。如果参数<code>allowND</code>的值为<code>true</code>，则该函数会尝试处理<code>CvMatND</code>实例，如果失败会抛出异常。如果<code>allowND</code>的值为<code>false</code>，参数<code>src</code>为<code>CvMatND</code>实例，则该函数会直接抛出异常。另外如果你缺失需要处理老版本中的兴趣通道<code>COI</code>，你可以使用函数<code>cv::extractImageCOI()</code>单独为这个感兴趣的像素通道创建新版本矩阵实例。</p>
<p>此外有时我们还需要将新版本实例转化为老版本的变量，将<code>cv::Mat</code>实例转换为老版本的<code>IplImage *</code>变量的方法如下。</p>
<pre><code>Cv::Mat A( 640, 480, cv::U8C3 );
// casting is implicit on assignment
IplImage.my_img = A;                 
iplImage* img = &my_img;
</code></pre>
<h5>cv::dct()</h5>
<p>该函数求原始矩阵的离散余弦变换或者离散余弦逆变换，其原型如下。该函数和一般的离散变换会在后文中会详细介绍，这里暂时先不用理解其原理和应用场景。</p>
<pre><code>// src：输入矩阵，必须是一维或者二维，向量长度必须是偶数，必要时可以填充数据
// dst：计算结果，和输入矩阵具有相同的尺寸
// flags：计算策略
// 可选值为DCT_INVERSE和DCT_ROWS，可以使用逻辑与符号同时选择
// DCT_INVERSE表示执行逆变换
// DCT_ROWS表示将矩阵视为n个一维行向量单独计算而不是二维向量整体计算
void cv::dct(cv::InputArray src,  cv::OutputArray dst, int flags);
</code></pre>
<p>该函数的效率和输入矩阵的尺寸密切相关，但是并不是一种单调关系。建议在使用该函数时，先使用函数<code>cv::getOptimalDFTSize()</code>获取到比输入数组更大的高效尺寸，并将输入数组扩展到这个大小。该函数在计算长度为n向量的离散余弦变换/逆变换时会依赖于n/2长度向量的离散傅立叶变换，因此正确的最佳输入矩阵尺寸计算方式如下。</p>
<pre><code>size_t opt_dft_size = 2 * cv::getOptimalDFTSize((N+1)/2);
</code></pre>
<h5>cv::dft()</h5>
<p>该函数求原始矩阵的离散傅立叶变换或者离散傅立叶逆变换，其原型如下。该函数和离散傅立叶变换背后的数学知识会在后文中会详细介绍，这里暂时先不用理解其原理和应用场景。</p>
<pre><code>// src：输入矩阵，必须是一维或者二维
// dst：计算结果矩阵，和输入矩阵具有相同的尺寸
// flags：计算策略标记
// nonzeroRows：有意义的行数
void cv::dft(cv::InputArray src, cv::OutputArray dst,
             int flags = 0, int nonzeroRows = 0);
</code></pre>
<p>通过设置参数flag时可以自定义计算过程，其可选值有<code>DFT_INVERSE</code>、<code>DFT_ROWS、DFT_SCALE</code>、<code>DFT_COMPLEX_OUTPUT</code>和<code>DFT_REAL_OUTPUT</code>，可以使用逻辑与符号组合多个策略。<code>DCT_INVERSE</code>表示执行逆变换。<code>DCT_ROWS</code>表示将矩阵视为n个一维行向量单独计算而不是二维向量整体计算。<code>DFT_SCALE</code>表示将计算结果除以矩阵的元素数量从而标准化数据。<code>DFT_SCALE</code>通常和<code>DFT_INVERSE</code>同时使用。因为这样保证了在计算逆的逆时将具有正确的标准化结果。</p>
<p><code>DFT_COMPLEX_OUTPUT</code>和<code>DFT_REAL_OUTPUT</code>非常有用，因为实数矩阵的傅立叶变换结果具有复数共轭对称性。因此即使得到的结果是复数，结果矩阵仍然和输入矩阵具有相同的元素个数，而不是它的两倍。这种包装是函数<code>cv::dft()</code>的默认行为，如果想要强制输出复数结果，则需要设置<code>DFT_COMPLEX_OUTPUT</code>标记。在计算离散傅立叶逆变换时，通常输入矩阵是复数矩阵，而输出结果也是复数矩阵，但是如果输入矩阵具有复数共轭对称性，或者说它就是实数矩阵计算离散傅立叶变换的结果，则其逆变换的结果也是一个实数矩阵。如果你在计算逆变换时能够确定输入矩阵的这种复数共轭对称性，并且你希望得到一个实数矩阵以其减少一半的内存使用量，则你可以设置<code>DFT_REAL_OUTPUT</code>标记。需要注意的是设置<code>DFT_REAL_OUTPUT</code>标记后，函数<code>cv::dft()</code>并不会真正去检查输入矩阵具有复数共轭对称性，仅仅只是假定其有这种性质。</p>
<p>参数<code>nonzeroRows</code>在被设置为非0值m时，如果执行离散傅立叶变换，则该函数会认为只有前m行是有意义的，如果执行离散傅立叶逆变换，则认为输出矩阵的前m行是非0的。该标记在计算卷积相关性时特别方便。</p>
<p>同样的，该函数的性能和输入矩阵的尺寸密切相关，并且这种关系不是单调的。因此建议在使用该函数时，先使用函数<code>cv::getOptimalDFTSize()</code>获取到比输入数组更大的高效尺寸，并将输入数组扩展到这个大小。</p>
<h5>cv::cvtColor()</h5>
<p>该函数将图像数据从1种颜色空间转换到另外一个颜色空间，并且保持元素的基本数据类型不变。其原型如下。该函数输入矩阵的基本元素类型可以是8或者16位无符号整型，或者是32位无符号浮点型数据，其处理的结果和元素矩阵保持相同的尺寸和元素的基本数据类型。参数<code>code</code>表示需要映射的颜色空间，会在下面的表格中介绍。参数<code>dstCn</code>指定输出结果的颜色通道数，如果选择默认值0，则将会根据原始数据和颜色空间转化类型两个因素决定处理结果中的颜色通道数。</p>
<pre><code>// src：输入数组
// dst：处理结果
// code：颜色映射的代码，具体见下面的表格
// dstCn：输出元素的颜色通道数，默认值为0
void cv::cvtColor(cv::InputArray src, cv::OutputArray dst,
                  int code, int dstCn = 0);
</code></pre>
<p>参数code的含义如下表。</p>
<table>
<thead>
<tr>
<th style="text-align:left">参数code的取值</th>
<th style="text-align:left">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left">cv::COLOR_BGR2RGB<br>cv::COLOR_RGB2BGR<br>cv::COLOR_RGBA2BGRA<br>cv::COLOR_BGRA2RGBA</td>
<td style="text-align:left">在RGB和BGR颜色空间中转化，可以包含alpha通道即透明度通道</td>
</tr>
<tr>
<td style="text-align:left">cv::COLOR_RGB2RGBA<br>cv::COLOR_BGR2BGRA</td>
<td style="text-align:left">为RGB和BGR颜色空间添加alpha通道</td>
</tr>
<tr>
<td style="text-align:left">cv::COLOR_RGBA2RGB<br>cv::COLOR_BGRA2BGR</td>
<td style="text-align:left">移除RGB和BGR颜色空间中的alpha通道</td>
</tr>
<tr>
<td style="text-align:left">cv::COLOR_RGB2BGRA<br>cv::COLOR_RGBA2BGR<br>cv::COLOR_BGRA2RGB<br>cv::COLOR_BGR2RGBA</td>
<td style="text-align:left">在RGB和BGR颜色空间中转化，并添加或者移除alpha通道</td>
</tr>
<tr>
<td style="text-align:left">cv::COLOR_RGB2GRAY<br>cv::COLOR_BGR2GRAY<br>cv::COLOR_RGBA2GRAY<br>cv::COLOR_BGRA2GRAY</td>
<td style="text-align:left">从RGB或BGR颜色空间转换到灰度数据，可选移除alpha通道</td>
</tr>
<tr>
<td style="text-align:left">cv::COLOR_GRAY2RGB<br>cv::COLOR_GRAY2BGR<br>cv::COLOR_GRAY2RGBA<br>cv::COLOR_GRAY2BGRA</td>
<td style="text-align:left">从灰度数据转换到RGB或BGR颜色空间，可选添加alpha通道</td>
</tr>
<tr>
<td style="text-align:left">cv::COLOR_RGB2BGR565<br>cv::COLOR_BGR2BGR565<br>cv::COLOR_BGR5652RGB<br>cv::COLOR_BGR5652BGR<br>cv::COLOR_RGBA2BGR565<br>cv::COLOR_BGRA2BGR565<br>cv::COLOR_BGR5652RGBA<br>cv::COLOR_BGR5652BGRA</td>
<td style="text-align:left">在RGB或BGR颜色空间和BGR565颜色空间之间相互转换，可以添加或者移除alpha通道</td>
</tr>
<tr>
<td style="text-align:left">cv::COLOR_GRAY2BGR565<br>cv::COLOR_BGR5652GRAY</td>
<td style="text-align:left">在灰度数据和BGR565颜色空间之间相互转换</td>
</tr>
<tr>
<td style="text-align:left">cv::COLOR_RGB2BGR555<br>cv::COLOR_BGR2BGR555<br>cv::COLOR_BGR5552RGB<br>cv::COLOR_BGR5552BGR<br>cv::COLOR_RGBA2BGR555<br>cv::COLOR_BGRA2BGR555<br>cv::COLOR_BGR5552RGBA<br>cv::COLOR_BGR5552BGRA</td>
<td style="text-align:left">在RGB或BGR颜色空间和BGR555颜色空间之间相互转换，可以添加或者移除alpha通道</td>
</tr>
<tr>
<td style="text-align:left">cv::COLOR_GRAY2BGR555<br>cv::COLOR_BGR5552GRAY</td>
<td style="text-align:left">在灰度数据和BGR555颜色空间之间相互转换</td>
</tr>
<tr>
<td style="text-align:left">cv::COLOR_RGB2XYZ<br>cv::COLOR_BGR2XYZ<br>cv::COLOR_XYZ2RGB<br>cv::COLOR_XYZ2BGR</td>
<td style="text-align:left">在RGB或BGR颜色空间和CIE XYZ颜色空间之间相互转换，CIE XYZ使用Rec709标准和D65白光源</td>
</tr>
<tr>
<td style="text-align:left">cv::COLOR_RGB2YCrCb<br>cv::COLOR_BGR2YCrCb<br>cv::COLOR_YCrCb2RGB<br>cv::COLOR_YCrCb2BGR</td>
<td style="text-align:left">在RGB或BGR颜色空间和亮度色度YCC颜色空间之间相互转换</td>
</tr>
<tr>
<td style="text-align:left">cv::COLOR_RGB2HSV<br>cv::COLOR_BGR2HSV<br>cv::COLOR_HSV2RGB<br>cv::COLOR_HSV2BGR</td>
<td style="text-align:left">在RGB或BGR颜色空间和HSV颜色空间之间相互转换</td>
</tr>
<tr>
<td style="text-align:left">cv::COLOR_RGB2HLS<br>cv::COLOR_BGR2HLS<br>cv::COLOR_HLS2RGB<br>cv::COLOR_HLS2BGR</td>
<td style="text-align:left">在RGB或BGR颜色空间和HLS颜色空间之间相互转换</td>
</tr>
<tr>
<td style="text-align:left">cv::COLOR_RGB2Lab<br>cv::COLOR_BGR2Lab<br>cv::COLOR_Lab2RGB<br>cv::COLOR_Lab2BGR</td>
<td style="text-align:left">在RGB或BGR颜色空间和CIE Lab颜色空间之间相互转换</td>
</tr>
<tr>
<td style="text-align:left">cv::COLOR_RGB2Luv<br>cv::COLOR_BGR2Luv<br>cv::COLOR_Luv2RGB<br>cv::COLOR_Luv2BGR</td>
<td style="text-align:left">在RGB或BGR颜色空间和CIE Luv颜色空间之间相互转换</td>
</tr>
<tr>
<td style="text-align:left">cv::COLOR_BayerBG2RGB<br>cv::COLOR_BayerGB2RGB<br>cv::COLOR_BayerRG2RGB<br>cv::COLOR_BayerGR2RGB<br>cv::COLOR_BayerBG2BGR<br>cv::COLOR_BayerGB2BGR<br>cv::COLOR_BayerRG2BGR<br>cv::COLOR_BayerGR2BGR</td>
<td style="text-align:left">从Bayer模式(单通道)数据转换到RGB或BGR颜色空间</td>
</tr>
</tbody>
</table>
<p>这里并不会详细的介绍这些颜色空间的差异，如需要了解可以移步至另一个篇文章<a href="https://www.jianshu.com/p/cdbca2e5720f" target="_blank">《数字媒体基础2-数字图像表示》</a>。现在只需要知道OpenCV提供了相关的函数能够处理这些颜色空间的数据转换。颜色空间转换隐含如下约定，8位位深度图像像素的取值范围为0到255，16位位深度图像像素的取值范围为0到65536，浮点型数据的取值范围为0.0到1.0。灰度图转换为颜色图时，所有的颜色通道值都相同，但是逆变换时采用了如下的加权计算公式。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="548" data-height="32"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-2a502b40ebc3d51c.png" data-original-width="548" data-original-height="32" data-original-format="image/png" data-original-filesize="15281" src="https://upload-images.jianshu.io/upload_images/1801561-2a502b40ebc3d51c.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>在HSV和HLS颜色空间中，色调(hue)的取值范围通常为[0, 360)，因此在8位位深度的图像中，记录色调值的时候需要记录其除2后的结果。</p>
<h5>cv::determinant()</h5>
<p>该函数计算一个满足特定需求的方阵行列式，其输入矩阵元素必须是单通道的，并且其基本数据类型必须是浮点型。如果输入矩阵的尺寸不大，会使用标准公式直接计算，如果输入的矩阵过大，会使用性能更高的高斯清除法(Gaussian elimination)计算。其原型如下。</p>
<pre><code>// mat：待计算矩阵
// return：输入矩阵的行列式
double cv::determinant(cv::InputArray mat);
</code></pre>
<p>如果确定一个矩阵是对称正定的，可以使用奇异值分解(Singular Value Decomposition, SVD)来求行列式，这个数学概念会在后续章节中详细介绍。需要注意的是使用这个技巧时需要将参数U和V都设置为NULL，然后就可以通过求矩阵W的乘积得到行列式结果。</p>
<h5>cv::divide()</h5>
<p>该函数计算标量和矩阵的商，它有两个形式，第一个形式的计算公式如下。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="544" data-height="78"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-f8c23fd56c7cfb06.png" data-original-width="544" data-original-height="78" data-original-format="image/png" data-original-filesize="20761" src="https://upload-images.jianshu.io/upload_images/1801561-f8c23fd56c7cfb06.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>其函数原型如下。</p>
<pre><code>void cv::divide(cv::InputArray src1, cv::InputArray src2, cv::OutputArray dst, 
                double scale = 1.0, int dtype = -1);
</code></pre>
<p>第二个形式的计算公式如下。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="548" data-height="50"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-2372e6c638f3bfb5.png" data-original-width="548" data-original-height="50" data-original-format="image/png" data-original-filesize="18120" src="https://upload-images.jianshu.io/upload_images/1801561-2372e6c638f3bfb5.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>其函数原型如下。</p>
<pre><code>void cv::divide(double scale, cv::InputArray src2, cv::OutputArray dst,
                int dtype = -1);
</code></pre>
<h5>cv::eigen()</h5>
<p>给定一个对策矩阵，该函数可以计算出其特征向量(Eigenvectors)和特征值(Eigenvalues)。该函数的输入矩阵元素基本数据类型必须是浮点型，计算结果特征值矩阵将以递减顺序包含输入矩阵的特质值。如果需要获取特征向量，则特征向量会按行的形式存储在矩阵中，并且其顺序和对应的特征值在特征值向量中的顺序相同。参数<code>lowindex</code>和<code>highindex</code>必须一起使用，它们共同决定了哪些特征值或者特征向量会被计算，如当这两个参数分别设置为0和1时，只有最大的两个特征向量才会被计算。该函数原型如下。</p>
<pre><code>bool cv::eigen(cv::InputArray src, cv::OutputArray eigenvalues,
               int lowindex = -1, int highindex = -1);

bool cv::eigen(cv::InputArray src, cv::OutputArray eigenvalues,
               cv::OutputArray eigenvectors,
               int lowindex = -1,int highindex = -1);
</code></pre>
<h5>cv::exp()</h5>
<p>该函数计算以自然对数e为底，输入矩阵中每个元素为指数的值，其原型如下。</p>
<pre><code>void cv::exp(cv::InputArray src, cv::OutputArray dst);
</code></pre>
<h5>cv::extractImageCOI()</h5>
<p>该函数从2.1版本之前的数组对象<code>arr</code>，如<code>IplImage</code>或者<code>CvMat</code>实例中提取兴趣通道(COI)。如果指定了参数<code>coi</code>，则提取对应的通道，如果未指定，则提取输入数组内部指定的兴趣通道。其原型如下。需要注意的是该函数仅仅用于兼容老版本OpenCV，如果使用现代版本的矩阵对象<code>cv::Mat</code>，请使用函数<code>cv::mixChannels()</code>或者<code>cv::split()</code>。</p>
<pre><code>bool cv::extractImageCOI(const CvArr* arr, cv::OutputArray dst, int coi = -1);
</code></pre>
<h5>cv::flip()</h5>
<p>该函数可以单独绕x轴或y轴对图像做镜像处理，也可以同时绕xy轴镜像图像。其原型如下。</p>
<pre><code>/// src：输入矩阵
/// dst：输出矩阵
/// flipCode：翻转参数
/// 小于0时，同时绕x轴和y轴做镜像。等于0时，绕x轴做镜像。大于0时绕y轴做镜像
void cv::flip(cv::InputArray src, cv::OutputArray dst, int flipCode = 0 );
</code></pre>
<h5>cv::gemm()</h5>
<p>该方法计算广义的矩阵乘法(Generalized matrix multiplication, GEMM)，可以实现矩阵乘法，转置后的矩阵乘法和带比例的乘法等。其原型如下。其中参数<code>flags</code>的取值可以是<code>cv::GEM_1_T</code>、<code>cv::GEM_2_T</code>和<code>cv::GEM_3_T</code>，以及他们之中的任意组合。所有的矩阵尺寸都应该满足矩阵乘法的要求，元素的基本数据类型都应该是浮点型。</p>
<pre><code>// src1：被乘数矩阵
// src2：乘数矩阵
// alpha：src1*src2结果的权重
// src3：偏移矩阵
// beta：偏移矩阵的权重
// dst：计算结果矩阵
// flags： 是否取输入矩阵的转置
void cv::gemm(cv::InputArray src1, cv::InputArray src2, double alpha,
              cv::InputArray src3, double beta,  
              cv::OutputArray dst, int flags = 0);
</code></pre>
<p>该函数的计算公式如下。其中和上面函数原型参数相同的变量表示相同的意思，op表示是否需要取矩阵转置后的结果。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="548" data-height="30"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-a0cb6245ff2b45bd.png" data-original-width="548" data-original-height="30" data-original-format="image/png" data-original-filesize="13423" src="https://upload-images.jianshu.io/upload_images/1801561-a0cb6245ff2b45bd.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>该函数还支持双通道的矩阵，其两个通道会被视为复数的两个部分。另外如下示例，该函数还可以直接使用矩阵表达式实现。</p>
<pre><code>cv::gemm(src1, src2, alpha, src3, bets, dst,cv::GEMM_1_T | cv::GEMM_3_T );
// 上面的函数等价于如下表达式
dst = alpha * src1.T() * src2 + beta * src3.T()
</code></pre>
<h5>cv::getConvertElem()和cv::getConvertScaleElem()</h5>
<p>这两个函数返回用于特定类型转换的函数的函数指针，其原型如下。其中通道数<code>cn</code>指的是内存连续的<code>fromType</code>类型的数量，这意味着对于连续存储的矩阵，你可以直接将该值设置为元素的个数从而一次处理整个矩阵。</p>
<pre><code>// fromType：原始基本数据类型，如cv::U8
// toType：目标基本数据类型，如CV_32F
// 返回值：返回下面的函数指针ConvertData
cv::convertData cv::getConvertElem(int fromType, int toType);

// from：带处理像素集合的内存地址
// to：存储处理后数据的内存地址
// cn：通道数
typedef void (*ConvertData)(const void* from, void* to, int cn);

// 返回值：返回下面的函数指针ConvertScaleData
cv::convertScaleData cv::getConvertScaleElem(int fromType, int toType);

// alpha：缩放系数
// beta：偏移值
// 需要主要的是缩放后偏移操作优先于类型转换操作
typedef void (*ConvertScaleData)(const void* from, void* to, int cn,
                                 double alpha, double beta);
</code></pre>
<h5>cv::idct()</h5>
<p>该函数计算某个矩阵的离散余弦逆变换，其原型如下。</p>
<pre><code>// flags：是否逐行按一维离散余弦逆变换公式计算
void cv::idct(cv::InputArray  src, cv::OutputArray dst, int flags);
</code></pre>
<p>也可以通过如下方式实现。</p>
<pre><code>cv::dct( src, dst, flags | cv::DCT_INVERSE );
</code></pre>
<h5>cv::inRange()</h5>
<p>该函数用于判断某个矩阵内部的元素是否位于指定的区间内，输出矩阵的基本数据类型为<code>cv::U8C1</code>，如果对应的元素位于指定的区间内，其值为255，否则为0。对于多通道矩阵而言，输出矩阵仍是单通道的，当对应元素的所有通道都位于指定的区间内时输出255，否则输出0。</p>
<pre><code>// upperb：区间上边界，包含该值
// lowerb：区间下边界，包含该值
void cv::inRange(cv::InputArray src, cv::InputArray upperb,
                 cv::InputArray lowerb, cv::OutputArray dst);
</code></pre>
<h5>cv::insertImageCOI()</h5>
<p>该函数用于和OpenCV2.1之前版本的数组对象(如<code>IplImage</code>和<code>CvMat</code>的实例)交互，它可以从<code>Cv::Mat</code>实例中读取数据，并将其写入到老版数组对象中的指定通道中。矩阵<code>img</code>和<code>arr</code>必须具有相同的尺寸，数据将会被拷贝至数组arr中。</p>
<pre><code>// img：源矩阵，必须是单通道
// arr：目标数组，OpenCV2.1之前版本的数组对象
// coi：指定的通道
void cv::insertImageCOI(cv::InputArray img, CvArr* arr, int coi = -1);
</code></pre>
<p>需要注意的是如果处理的是新版本矩阵对象，需要使用<code>cv::merge()</code>合并矩阵。</p>
<h5>cv::invert()</h5>
<p>该函数求矩阵的逆，矩阵src的基本数据类型必须是浮点型，因为该函数有计算伪逆(Pseudo-inverses)的可能，输入矩阵<code>src</code>可以不是方阵。该函数支持多种计算逆矩阵的方法，可以通过参数<code>method</code>控制，这些方法列举如下表，函数返回值取决于使用的方法。</p>
<pre><code>// 如果矩阵src是奇异矩阵(Singular Matrix)，则返回0
// method：使用的计算方法
double cv::invert(cv::InputArray src, cv::OutputArray dst,
                  int method = cv::DECOMP_LU);
</code></pre>
<p>参数method的取值及其含义如下表。</p>
<table>
<thead>
<tr>
<th style="text-align:left">参数method的取值</th>
<th style="text-align:left">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left">cv::DECOMP_LU</td>
<td style="text-align:left">高斯消除法(LU分解)</td>
</tr>
<tr>
<td style="text-align:left">cv::DECOMP_SVD</td>
<td style="text-align:left">奇异值分解(Singular value decomposition, SVD)</td>
</tr>
<tr>
<td style="text-align:left">cv::DECOMP_CHOLESKY</td>
<td style="text-align:left">只用于对称正定矩阵</td>
</tr>
</tbody>
</table>
<p>在使用<code>cv::DECOMP_LU</code>方法时，函数返回值为矩阵<code>src</code>的行列式，如果该值为0，则求逆计算失败，矩阵dst的所有元素都为0。如果使用<code>cv::DECOMP_SVD</code>方法，则函数返回值是矩阵逆条件数量(即最小和最大特征值的比)。如果此时矩阵<code>src</code>是奇异的，则该函数会计算矩阵的伪逆。方法<code>cv::DECOMP_SVD</code>和<code>cv::DECOMP_CHOLESKY</code>要求矩阵<code>src</code>必须是方阵，并且是非奇异正定的。</p>
<h5>cv::log()</h5>
<p>该函数计算矩阵src中每个元素的自然对数，对于值等于或者小于0时，矩阵<code>dst</code>中对应的元素将会被填充为一个较大负值。其原型如下。</p>
<pre><code>void cv::log(cv::InputArray src, cv::OutputArray dst);
</code></pre>
<h5>cv::LUT()</h5>
<p>该函数通过<code>src</code>矩阵中定义的索引值到lut矩阵中查找对应的元素，将结果放到矩阵dst中。矩阵src的基本数据类型位深度为8位，如果是8位无符号整数，则该函数在计算时会在这个索引值的基础上加128，使之刚好位于矩阵lut的索引区间内。矩阵<code>lut</code>应该包含256个元素，它可以是单通道或者和矩阵<code>src</code>具有相同的通道数。</p>
<p>当矩阵<code>src</code>为多通道，<code>lut</code>为单通道时，则索引矩阵<code>src</code>中每个元素的每个通道索引都会在<code>lut</code>的单个通道中查询映射值。如果此时<code>lut</code>为多通道，则<code>src</code>的每个元素的索引值队在<code>lut</code>的对应通道中查询映射值。该函数原型如下。</p>
<pre><code>void cv::LUT(cv::InputArray src, cv::InputArray lut, cv::OutputArray dst);
</code></pre>
<h5>cv::magnitude()</h5>
<p>该函数主要用于计算二维向量场中笛卡尔坐标系向极坐标系(极坐标系中的每个点由到极点的距离和夹角表示)转换时该点到极点的距离。即将矩阵x和矩阵y对应值求平方和后的结果开发再赋值给矩阵dst中对应的元素。该函数原型如下。</p>
<pre><code>void cv::magnitude(cv::InputArray x, cv::InputArray y, cv::OutputArray dst);
</code></pre>
<h5>cv::Mahalanobis()</h5>
<p>该函数计算某个点(样本)的<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fblog.csdn.net%2Fu010167269%2Farticle%2Fdetails%2F51627338" target="_blank">马氏距离</a>(Mahalanobis distance)，马氏距离的定义是样本集中的某个点到该样本的高斯分布中心的向量距离，以该高斯分布的逆协方差作为度量来计算，如下图。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1096" data-height="922"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-173650e384dcd8eb.png" data-original-width="1096" data-original-height="922" data-original-format="image/png" data-original-filesize="133669" src="https://upload-images.jianshu.io/upload_images/1801561-173650e384dcd8eb.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>图中，三个椭圆上所有样本到分布中心的距离分别为1.0、2.0和3.0。直观上看，这类似基础统计学中的标准分数(z-core)，即某个一维点到分布中心的距离是由该分布的方差作为单位衡量的，而马氏距离可以认为是该思路在高维空间中的推广。马氏距离的计算公式如下，其中向量x表示一个n维样本中任意一点，向量μ中元素表示n维样本中对应维度的均值，∑-1表示n维样本的逆协方差矩阵。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="540" data-height="48"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-026124beb4bbf2d5.png" data-original-width="540" data-original-height="48" data-original-format="image/png" data-original-filesize="14163" src="https://upload-images.jianshu.io/upload_images/1801561-026124beb4bbf2d5.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>函数<code>cv::Mahalanobis()</code>的原型如下。</p>
<pre><code>// vec1：样本矩阵，大小为m*1，表示一个样本点
// vec2：均值矩阵，大小为m*1，表示在m个维度上的均值
// vec3：协方差逆矩阵，大小为m*m，位m个维度上的原始样本集合协方差矩阵
double cv::mahalanobis(cv::InputArray vec1, cv::InputArray vec2, 
                       cv::InputArray icovar);
</code></pre>
<p>使用该函数参数化简上述公式后可以得到如下公式。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1138" data-height="120"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-09e2bdaa4c4b65fc.png" data-original-width="1138" data-original-height="120" data-original-format="image/png" data-original-filesize="18421" src="https://upload-images.jianshu.io/upload_images/1801561-09e2bdaa4c4b65fc.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>在使用该函数时需要传入参数逆协方差矩阵，可以使用函数<code>cv::calcCovarMatrix()</code>先计算出原始样本集的协方差矩阵，再使用函数<code>cv::invert()</code>和参数<code>cv::DECOMP_SVD</code>计算其逆矩阵。使用参数<code>cv::DECOMP_SVD</code>是一个好的编程习惯，因为你可能遇到一个包含奇异值0的分布。</p>
<h5>cv::max()</h5>
<p>该系列函数逐元素比较一个矩阵中所有元素与另外一个矩阵中对应元素，或者与一个标量的大小，返回一个矩阵表达式或者将结果写入到指定的矩阵中，它们原型如下。</p>
<pre><code>// 返回值：矩阵表达式
// src1和src2是两个待比较的矩阵
cv::MatExpr cv::max(const cv::Mat& src1, const cv::Mat& src2);
// 矩阵元素和标量比较
MatExpr cv::max(const cv::Mat&  src1,  double value);
// 标量和矩阵元素比较
MatExpr cv::max(double value, const cv::Mat&  src1);

// 将比较结果写入到指定矩阵中
void cv::max(cv::InputArray src1, cv::InputArray src2, cv::OutputArray dst);
void cv::max(const Mat& src1, const Mat& src2, Mat& dst);
void cv::max(const Mat& src1, double value, Mat& dst);
</code></pre>
<h5>cv::mean()</h5>
<p>该函数计算了输入数组中没有被蒙版遮住的所有像素的平均值，如果输入矩阵元素是多通道的，则每个通道都会被单独计算。函数原型如下。</p>
<pre><code>cv::Scalar cv::mean(cv::InputArray src, cv::InputArray  mask = cv::noArray());
</code></pre>
<h5>cv::meanStdDev()</h5>
<p>该函数计算矩阵的均值和标准差，如果矩阵元素包含多个通道，则每个通道会被单独计算，返回的矩阵尺寸为m✖️1，m是输入矩阵中元素的通道数。参数mask为蒙版矩阵，在计算矩阵和方差时如果该矩阵中的元素为非零值，则输入矩阵的元素不会被列入计算范围，即计算均值时统计的总元素数也不包含该矩阵。函数原型如下。</p>
<pre><code>void cv::meanStdDev(cv::InputArray src, cv::OutputArray mean, 
                    cv::OutputArray stddev, cv::InputArray mask = cv::noArray());
</code></pre>
<h5>cv::merge()</h5>
<p>该函数是函数<code>cv::split()</code>的反向操作，它将多个矩阵合并为1个矩阵。其函数原型如下。</p>
<pre><code>// mv：待合并的C语音风格的矩阵数组
// count：矩阵数组中矩阵个数
// dst：合并结果
void cv::merge(const cv::Mat* mv, size_t count, cv::OutputArray dst);

// mv：待合并的STL风格的矩阵数组
void merge(const vector<cv::Mat>& mv, cv::OutputArray dst);
</code></pre>
<h5>cv::min()</h5>
<p>该函数取矩阵对另外一个矩阵中对应元素，或者对某个特定值比较后的最小值，返回一个矩阵表达式或者将结果写入到指定的矩阵中。函数原型如下。</p>
<pre><code>// 返回值：矩阵表达式
// src1和src2是两个待比较的矩阵
cv::MatExpr cv::min(const cv::Mat& src1, const cv::Mat& src2);
// 矩阵元素和标量比较
MatExpr cv::min(const cv::Mat& src1, double value);
// 标量和矩阵元素比较
MatExpr cv::min(double value, const cv::Mat& src1);

// 将比较结果写入到指定矩阵中
void cv::min(cv::InputArray src1, cv::InputArray src2, cv::OutputArray dst);
void cv::min(const Mat& src1, const Mat& src2, Mat& dst);
void cv::min(const Mat& src1, double value, Mat& dst);
</code></pre>
<h5>cv::minMaxIdx()</h5>
<p>这类函数查找矩阵中的最大和最小值，将它们及它们的索引写入到指定的地址中。该函数可以用于处理任意维度的矩阵和稀疏矩阵。在处理稀疏矩阵时，只处理其中的有效数据，也就是广义的非零元素，但是需要注意的是，在稀疏矩阵的操作过程中可能存在值为0的有效元素。具体可以参考前面章节的稀疏矩阵介绍，这部分值为0的有效元素也会被纳入到统计中。该函数原型如下。</p>
<pre><code>// src：待查询矩阵，只能是单通道
// minVal和maxVal：最小值和最大值写入地址，不能为NULL
// minIdx和maxIdx：最小值和最大值索引的写入地址，可传NULL
// mask：蒙版矩阵
void cv::minMaxIdx(cv::InputArray src, double* minVal, double* maxVal,
                   int* minIdx, int* maxIdx, cv::InputArray mask = cv::noArray());

void cv::minMaxIdx(const cv::SparseMat& src, double* minVal, double* maxVal,
                   int* minIdx, int* maxIdx);
</code></pre>
<p>需要注意的是在输入元素是一维矩阵的情况下，用于存储最值索引的参数<code>minVal</code>和<code>maxVal</code>也必须是分配了2位双精度浮点型数据的内存地址。这是因为该函数使用了这样一个惯例，单维数组本质上是一个M✖️1点矩阵，此时返回的索引值第二个元素总为0。</p>
<h5>cv::mixChannels()</h5>
<p>该函数可以从一个或者多个输入图像中读取数据，对通道进行重排列并将其写到一个或者多个矩阵中，OpenCV中有很多操作也是这个问题的特殊情况。例如像<code>cv::split()</code>和<code>cv::merge()</code>或者<code>cv::cvtColor()</code>中的部分场景，这些方法的底层都调用了函数<code>cv::mixChannels()</code>。该函数的输入矩阵可以是多通道的，函数会按照指定的方式将原始数据中的通道映射到输出矩阵中。函数的原型如下。</p>
<pre><code>// srcv：原始数据矩阵数组的地址
// nsrc：原始数据矩阵的个数
// dstv：目标矩阵数组地址
// ndst：目标矩阵的个数
// fromTo：映射关系数组地址，每对映射关系包含表示from和to的两个整型变量，该参数在下文详细介绍
// n_pairs：映射关系的个数（按映射关系对计数）
void cv::mixChannels(const cv::Mat* srcv, int nsrc,
                     cv::Mat* dstv, int ndst,
                     const int* fromTo, size_t n_pairs);

// srcv：包含多个原始数据矩阵的向量
// dstv：包含多个目标数据矩阵的向量
void cv::mixChannels(const vector<cv::Mat>& srcv, vector<cv::Mat>& dstv,
                     const int* fromTo, size_t n_pairs);
</code></pre>
<p>参数<code>fromTo</code>控制了通道的映射关系，它指向的int型数组中每两个元素表示一组映射关系，即将源数据中的某个矩阵的某个通道映射到目标数据中的某个矩阵的某个通道中。元素数据目标矩阵通道的编号分别从输入和输出矩阵数组中的第一个矩阵的第一个通道开始，从0开始编号，没隔一个通道，编号加1。映射关系如下图所示。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1096" data-height="678"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-76c488c8de120a37.png" data-original-width="1096" data-original-height="678" data-original-format="image/png" data-original-filesize="115604" src="https://upload-images.jianshu.io/upload_images/1801561-76c488c8de120a37.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>需要注意的是和OpenCV2.1以后的大多数函数不同，该函数不会为输出矩阵数组分配内存空间，在调用该函数时必须预先分配好合适的内存空间。</p>
<h5>cv::mulSpectrums()</h5>
<p>该函数对两个傅立叶频谱矩阵执行逐元素乘法操作，并将结果写入到指定的矩阵中。函数原型如下。</p>
<pre><code>// arr1和arr2：待计算的两个傅立叶频谱矩阵，它们需要具有相同的尺寸
// dst：计算结果
// flags：用于标记待计算矩阵时按行向量处理为1维频谱向量还是二维频谱矩阵
// 前者该值设置为cv::DFT_ROWS，后者设置为0
// conj：标记是否使用第二个矩阵的共轭矩阵和第一个矩阵进行计算
void cv::mulSpectrums(cv::InputArray arr1, cv::InputArray arr2,
                      cv::OutputArray dst, int flags, bool conj = false);
</code></pre>
<h5>cv::multiply()</h5>
<p>该函数逐元素的求两个矩阵的乘积，并在最后施加一个缩放系数。其原型如下。</p>
<pre><code>// scale：全局缩放系数
// dtype：输出矩阵元素的数据类型
void cv::multiply(cv::InputArray src1, cv::InputArray src2,
                  cv::OutputArray dst, double scale = 1.0, int dtype = -1);
</code></pre>
<h5>cv::mulTransposed()</h5>
<p>当参数<code>aTa</code>为<code>ture</code>时，该函数计算矩阵转置和自己的乘积，当参数<code>aTa</code>为<code>false</code>时该函数计算矩阵和自己转置的乘积，其原型如下。参数<code>src1</code>必须是两维单通道的矩阵，但是基本数据类型不限定必须是浮点型。如果参数<code>dtype</code>使用默认值，则计算得到的矩阵基本数据类型和输入矩阵相同，此外<code>dtype</code>还可以指定为<code>cv::F64</code>或者为<code>CV_32F</code>从而指定计算结果矩阵的基本数据类型。</p>
<pre><code>void cv::mulTransposed(cv::InputArray src1, cv::OutputArray dst,
                       bool aTa, cv::InputArray delta = cv::noArray(), 
                       double scale = 1.0, int dtype = -1);
</code></pre>
<p>根据上面函数原型中的参数，其计算公式如下。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="824" data-height="100"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-54713912625c06cc.png" data-original-width="824" data-original-height="100" data-original-format="image/png" data-original-filesize="37549" src="https://upload-images.jianshu.io/upload_images/1801561-54713912625c06cc.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h5>cv::norm()</h5>
<p>不包含参数<code>src2</code>时，该函数用于求单个矩阵的范数，包含参数<code>src2</code>时，该函数用于求两个矩阵之间的距离范数。另外这些函数也能处理稀疏矩阵，需要注意的是此时将忽略值为0的元素。函数原型如下。</p>
<pre><code>// normType：需要计算的范数类型，详细见下表
// mask：蒙版矩阵
double cv::norm(cv::InputArray src1, int normType = cv::NORM_L2,
                cv::InputArray mask = cv::noArray());

double cv::norm(cv::InputArray src1, cv::InputArray src2, 
                int normType = cv::NORM_L2,
                cv::InputArray mask = cv::noArray());

double cv::norm(const cv::SparseMat& src, int normType = cv::NORM_L2);
</code></pre>
<p>对于处理单个矩阵的函数而言，参数<code>normType</code>的可选值及范数计算公式如下图。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="704" data-height="540"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-f7a47bdc8f13d7a4.png" data-original-width="704" data-original-height="540" data-original-format="image/png" data-original-filesize="121991" src="https://upload-images.jianshu.io/upload_images/1801561-f7a47bdc8f13d7a4.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>对于处理两个矩阵的函数而言，参数<code>normType</code>的可选值及范数计算公式如下图。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="932" data-height="978"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-34742fc1c2ecd624.png" data-original-width="932" data-original-height="978" data-original-format="image/png" data-original-filesize="235007" src="https://upload-images.jianshu.io/upload_images/1801561-34742fc1c2ecd624.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>对于所有的计算范数的函数，如果输入矩阵包含多通道，则将上面两个图中的计算公式中<code>src1i</code>或者<code>src2i</code>表示的都是第i个元素的多个通道之和。另外，在计算两个矩阵的距离范数时，参数<code>src2</code>和<code>src1</code>必须有相同的尺寸和通道数。</p>
<h5>cv::normalize()</h5>
<p>该函数可以将元素矩阵元素的值映射到指定的区间内，如果指定的区间为[0, 1]，则该操作为标准化操作。输出矩阵<code>dst</code>的尺寸和输入矩阵<code>src</code>相同，在参数<code>dtype</code>未指定时它们还有相同的基本数据类型。参数<code>dtype</code>可以设置为如<code>CV_32F</code>等OpenCV的基本数据类型。这类函数的原型如下。</p>
<pre><code>// alpha和beta根据参数normType的不同有不同的含义，具体见下图
// normType：标准化策略，具体见下图
// dtype：输出矩阵的基本数据类型
// mask：蒙版矩阵
void cv::normalize(cv::InputArray src1, cv::OutputArray dst,
                   double alpha = 1, double beta = 0, int normType = cv::NORM_L2,
                   int dtype = -1, cv::InputArray  mask  = cv::noArray());

void cv::normalize(const cv::SparseMat& src, cv::SparseMat& dst,
                   double alpha = 1, int normType = cv::NORM_L2);
</code></pre>
<p>参数<code>normType</code>表示标准化策略，其可用的取值和含义如下图。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="798" data-height="388"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-d41bf38eb9ef423d.png" data-original-width="798" data-original-height="388" data-original-format="image/png" data-original-filesize="66754" src="https://upload-images.jianshu.io/upload_images/1801561-d41bf38eb9ef423d.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>当参数<code>normType</code>指定为<code>cv::NORM_INF</code>时，矩阵将被缩放至其最大元素的绝对值和参数<code>alpha</code>的值相同。当参数<code>normType</code>指定为<code>cv::NORM_L1</code>或<code>cv::NORM_L2</code>时，矩阵将被缩放至其对应的范数和参数<code>alpha</code>的值相同。当参数<code>normType</code>指定为<code>cv::NORM_MINMAX</code>时，矩阵将被缩放使得所有的元素都被线性映射至参数<code>alpha</code>和<code>beta</code>指定的闭区间内。需要注意的是在处理稀疏矩阵时<code>cv::NORM_MINMAX</code>不可用，这是因为该模式会处理稀疏矩阵内的值为0元素，可能使所有元素变为非零值，将稀疏矩阵变为非稀疏矩阵，从而影响矩阵稀疏性。</p>
<h5>cv::perspectiveTransform()</h5>
<p>该函数计算一些列点的投影变换，其原型如下。参数src必须是双通道或者三通道的矩阵，而参数<code>mtx</code>则必须分别是3✖️3或者4✖️4的投影矩阵。在计算过程中都会将矩阵<code>src</code>中的每个元素认为是1个点，并为其补充1个值为1点通道，将点的坐标从笛卡尔坐标扩充至齐次坐标系(Homogeneous Coordinates)。然后将每个点和投影矩阵相乘，并求所有非扩展通道的值和扩展通道值的商，将得到的结果放入指定的矩阵中。</p>
<pre><code>void cv::perspectiveTransform(cv::InputArray src, cv::OutputArray dst, 
                              cv::InputArray mtx);
</code></pre>
<p>每个元素和投影矩阵相乘的公式如下。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="332" data-height="548"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-e76468214f4e18ba.png" data-original-width="332" data-original-height="548" data-original-format="image/png" data-original-filesize="101969" src="https://upload-images.jianshu.io/upload_images/1801561-e76468214f4e18ba.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>需要注意的是该方法用于转换一系列的点而不是图像，如果你想要对一个图像应用透视变换，实际上是想将其从一个位置移动到另外一个位置，你应该调用函数<code>cv::warpPerspective()</code>。如果想要解决投影变换逆问题，即通过一些列转换前后的点对来找到最有可能的投影矩阵，可以使用函数<code>cv::getPerspectiveTransform()</code>或者<code>cv::findHomography()</code>。</p>
<h6>cv::phase()</h6>
<p>该函数用于计算在二维向量场上点从笛卡尔坐标向极坐标转换后的方位角。其原型如下。该向量场又两个单通道矩阵组成，即参数x和y中对应的元素，你可以使用函数<code>cv::split()</code>将多通道矩阵拆分为单通道矩阵。这两个矩阵应该有相同的尺寸。</p>
<pre><code>// angleInDegrees：计算结果的表示单位
// ture单位为角度，false单位为弧度
void cv::phase(cv::InputArray x, cv::InputArray y,
               cv::OutputArray dst, bool angleInDegrees = false);
</code></pre>
<p>该函数内部的计算公式如下。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="274" data-height="36"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-70e4c4aaaadcd746.png" data-original-width="274" data-original-height="36" data-original-format="image/png" data-original-filesize="9387" src="https://upload-images.jianshu.io/upload_images/1801561-70e4c4aaaadcd746.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h5>cv::polarToCart()</h5>
<p>该函数通过两个输入矩阵中对应位置的元素组成一个二维向量，将其表示为一个极坐标，并计算其对应的笛卡尔坐标，将结果保持在两个输出矩阵中。其原型如下。</p>
<p>参数<code>magnitude</code>和<code>angle</code>分别保存极坐标的幅度和角度(角度和弧度通过参数<code>angleInDegrees</code>指定，该参数为<code>ture</code>时保存的是角度，<code>false</code>表示保存的是弧度)，因此这两个矩阵需要有相同的尺寸和基本数据类型。参数x和y也具有相同的尺寸，它们分别保存了笛卡尔坐标的两个分量。</p>
<pre><code>void cv::polarToCart(cv::InputArray magnitude, cv::InputArray angle, 
                     cv::OutputArray x, cv::OutputArray y,
                     bool angleInDegrees = false);
</code></pre>
<p>该函数内部的计算公式如下。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="546" data-height="140"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-a43cad6d0f900650.png" data-original-width="546" data-original-height="140" data-original-format="image/png" data-original-filesize="34041" src="https://upload-images.jianshu.io/upload_images/1801561-a43cad6d0f900650.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h5>cv::pow()</h5>
<p>该函数计算矩阵中每个元素的指数幂，其原型如下。当p为整数时，函数直接进行幂运算，否则将先求原始数据的绝对值，再进行幂运算，这样得到的结果一定是实数。对于一些特殊的p值，如整数或者±1/2，该函数内部会用到特殊的算法提高运算效率。</p>
<pre><code>void cv::pow(cv::InputArray src, double p, cv::OutputArray dst);
</code></pre>
<h5>cv::randu()</h5>
<p>这类函数用于计算随机数，第一种形式是一个模版函数。该函数会返回指定类型均匀分布的随机数，其取值范围从为[0, 该类型的最大值) ，对于浮点数而言取值范围为[0.0, 1.0)。需要注意的是该模版函数返回值只包含单个有效数，即对<code>cv::randu<Vec4f></code>调用该函数返回值除第一个元素外都为0。该类型函数原型如下。</p>
<pre><code>template<typename _Tp>
_Tp randu(); 
</code></pre>
<p>第二种形式可以为一个已经分配好内存的矩阵填充指定范围的随机数，参数low和high表示的矩阵应为1✖️1的4通道矩阵或者1✖️4的单通道矩阵，也可以直接传递一个<code>cv::Scalar</code>的实例。得到的随机数区间为[low，high)。该函数原型如下。另外在创建随机数和填充矩阵时可以考虑使用类<code>cv::RNG</code>。</p>
<pre><code>void cv::randu(cv::InputOutArray mtx,
               cv::InputArray low, cv::InputArray high);
</code></pre>
<h5>cv::randn()</h5>
<p>该函数使用正太分布的随机数填充矩阵，其原型如下。参数<code>mean</code>和<code>stddev</code>分别指定了随机变量分布的均值和标准差。参数<code>mtx</code>中的每个元素的每个通道会被独立计算，因此如果参数<code>mtx</code>通道数为4，则参数<code>mean</code>和<code>stddev</code>应当为1✖️4单通道，或者1✖️1四通道矩阵，或者是<code>cv::Scalar</code>的实例。</p>
<pre><code>void cv::randn(cv::InputOutArray mtx, cv::InputArray mean, cv::InputArray stddev);
</code></pre>
<h5>cv::randShuffle()</h5>
<p>该函数随机选择一维矩阵中的一对元素，并交换它们的位置，从而随机化这个矩阵。交换的次数等于参数<code>mtx</code>中的元素个数和参数<code>iterFactor</code>的乘积。参数<code>rng</code>是随机数生成器，如果未提供，该函数内部会调用函数<code>theRNG()</code>使用默认的随机数生成器。其原型如下。</p>
<pre><code>void cv::randShuffle(cv::InputOutArray mtx, double iterFactor = 1,
                     cv::RNG* rng = NULL);
</code></pre>
<h5>cv::reduce()</h5>
<p>该函数通过指定的不同行或者不同列的合并规则，将矩阵最终简化为一个n✖️1或者1✖️n的向量，其原型如下。</p>
<pre><code>void cv::reduce(cv::InputArray src, cv::OutputArray vec,
                int dim, int reduceOp = cv::REDUCE_SUM, int dtype = -1);
</code></pre>
<p>参数<code>dim</code>定义了合并的方式，其可取的值和含义如下表。</p>
<table>
<thead>
<tr>
<th style="text-align:left">参数dim的取值</th>
<th style="text-align:left">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left">0</td>
<td style="text-align:left">不同行之间合并，最后输出仅1行的矩阵</td>
</tr>
<tr>
<td style="text-align:left">1</td>
<td style="text-align:left">不同列之间合并，最后输出仅1列的矩阵</td>
</tr>
</tbody>
</table>
<p>参数<code>reduceOp</code>定义了不同元素的合并规则，其可取的值和含义如下表。</p>
<table>
<thead>
<tr>
<th style="text-align:left">参数reduceOp的取值</th>
<th style="text-align:left">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left">cv::REDUCE_SUM</td>
<td style="text-align:left">求和</td>
</tr>
<tr>
<td style="text-align:left">cv::REDUCE_AVG</td>
<td style="text-align:left">计算均值</td>
</tr>
<tr>
<td style="text-align:left">cv::REDUCE_MAX</td>
<td style="text-align:left">取极大值</td>
</tr>
<tr>
<td style="text-align:left">cv::REDUCE_MIN</td>
<td style="text-align:left">取极小值</td>
</tr>
</tbody>
</table>
<p>该函数支持所有基本数据类型的多通道的矩阵，在使用<code>cv::REDUCE_SUM</code>和<code>cv::REDUCE_AVG</code>合并规则时将参数<code>dtype</code>设置为一个高精度的数据类型很有必要，因为这样能够避免在数据累加可能出现的溢出类累积问题。</p>
<h5>cv::repeat()</h5>
<p>该函数重复拷贝某个矩阵内指定的行和列直至达到指定的拷贝次数。其原型如下。</p>
<pre><code>// src：数据源，一个二维矩阵
// nx和ny：在x和y方向上的拷贝次数
// dst：需要填充的矩阵，他的尺寸和矩阵src无任何关联，可以不同
void cv::repeat(cv::InputArray src, int nx, int ny, cv::OutputArray dst);

// 返回值：返回拷贝得到的矩阵
cv::Mat cv::repeat(cv::InputArray src, int nx, int ny);
</code></pre>
<h5>cv::scaleAdd()</h5>
<p>该函数求两个矩阵的和，其原型如下。</p>
<pre><code>// src1：被加数，矩阵src1
// scale：计算时对矩阵src1的缩放值
// src2：加数
// dst：用于保存计算结果的输出矩阵
void cv::scaleAdd(cv::InputArray src1, double scale, cv::InputArray src2, 
                  cv::OutputArray dst);
</code></pre>
<p>该函数也可以通过如下矩阵表达式直接实现。</p>
<pre><code>dst = scale * src1 + src2;
</code></pre>
<h5>cv::setIdentity()</h5>
<p>该函数将矩阵中所有行列索引不相等的元素设置为0，将所有行列索引相等的元素设置为指定的值，其原型如下。该函数可以处理包含任意基本数据类型，任意尺寸的矩阵。</p>
<pre><code>void cv::setIdentity(cv::InputOutputArray dst, 
                     const cv::Scalar& value = cv::Scalar(1.0));
</code></pre>
<p>在处理<code>cv::Ma</code>t实例时，求单位矩阵通常使用其成员函数<code>cv::Mat eye()</code>。</p>
<h5>cv::solve()</h5>
<p>该函数基于函数<code>cv::invert()</code>求解一个线性系统，找到最优解，其原型如下。</p>
<pre><code>// lhs：线性系统样本坐标集合，n✖️n矩阵
// rhs：线性系统右侧常量部分，n✖️1矩阵
// dst：线性系统系数的最优解，n✖️1矩阵
// method：求解方法，稍后详细介绍

int cv::solve(cv::InputArray lhs, cv::InputArray rhs,
              cv::OutputArray dst, int method = cv::DECOMP_LU);
</code></pre>
<p>该函数内部的计算公式如下。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="548" data-height="50"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-3782f149e7bf0a25.png" data-original-width="548" data-original-height="50" data-original-format="image/png" data-original-filesize="13520" src="https://upload-images.jianshu.io/upload_images/1801561-3782f149e7bf0a25.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>其中A是参数<code>lhs</code>传入的方阵，B是参数<code>rhs</code>传入的向量，C是该函数内部根据参数<code>method</code>选取的策略计算的一个中间值，目的是为了寻找最优的向量X，向量X将会写入到参数<code>dst</code>中。该函数只能处理浮点型的数据，函数返回值为非0值时表示该函数能够计算该线性系统的解，反之则不能。参数<code>method</code>可能的取值及其含义如下表。</p>
<table>
<thead>
<tr>
<th style="text-align:left">参数method的取值</th>
<th style="text-align:left">含义</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left">cv::DECOMP_LU</td>
<td style="text-align:left">高斯消元法（LU分解）</td>
</tr>
<tr>
<td style="text-align:left">cv::DECOMP_SVD</td>
<td style="text-align:left">奇异值分解（SVD）</td>
</tr>
<tr>
<td style="text-align:left">cv::DECOMP_CHOLESKY</td>
<td style="text-align:left">处理对称正定矩阵</td>
</tr>
<tr>
<td style="text-align:left">cv::DECOMP_EIG</td>
<td style="text-align:left">特征值分解，只能处理对称矩阵</td>
</tr>
<tr>
<td style="text-align:left">cv::DECOMP_QR</td>
<td style="text-align:left">QR因式分解</td>
</tr>
<tr>
<td style="text-align:left">cv::DECOMP_NORMAL</td>
<td style="text-align:left">可选附加标志，表示求解标准方程</td>
</tr>
</tbody>
</table>
<p>参数<code>cv::DECOMP_LU</code>和<code>cv::DECOMP_CHOLESKY</code>不能用于处理奇异矩阵，在使用这两个参数时，如果输入矩阵lhs是奇异矩阵，则该函数立即结束并返回0，否则返回1。可以使用<code>cv::DECOMP_QR</code>或者<code>cv::DECOMP_SVD</code>找到线性系统的<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FLeast_squares" target="_blank">最小二分解</a>(Least-squares solution)从而处理超定线性系统(无解的线性系统，通常使用最优解拟合)。这两种方法可以处理奇异的输入矩阵<code>lhs</code>。</p>
<p>上表的前5个选项都是互斥的，但是最后一个选项是可以通过逻辑与符号与前面的任意一个选项叠加。该选项被叠加时，该函数会尝试求标准方程组(Normal Equations)的解，否则求一般方程组(Normal Equations)的解。即未叠加该选项时的标准方程组如下。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="540" data-height="50"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-210e2e4b1e7c7431.png" data-original-width="540" data-original-height="50" data-original-format="image/png" data-original-filesize="10854" src="https://upload-images.jianshu.io/upload_images/1801561-210e2e4b1e7c7431.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>未叠加该选项时的一般方程组如下。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="332" data-height="44"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-f233f160e1d93eb0.png" data-original-width="332" data-original-height="44" data-original-format="image/png" data-original-filesize="9896" src="https://upload-images.jianshu.io/upload_images/1801561-f233f160e1d93eb0.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h5>cv::solveCubic()</h5>
<p>该函数用于求解三次多项式的实根，其原型如下。</p>
<pre><code>int cv::solveCubic(cv::InputArray coeffs, cv::OutputArray roots);
</code></pre>
<p>如果参数coeffs包含四个元素，则多项式表示如下。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="826" data-height="58"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-ea829f344a8c9fa6.png" data-original-width="826" data-original-height="58" data-original-format="image/png" data-original-filesize="20337" src="https://upload-images.jianshu.io/upload_images/1801561-ea829f344a8c9fa6.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>如果参数coeffs包含三个元素，则多项式表示如下。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="818" data-height="66"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-c2b4bfba2426e6b9.png" data-original-width="818" data-original-height="66" data-original-format="image/png" data-original-filesize="22750" src="https://upload-images.jianshu.io/upload_images/1801561-c2b4bfba2426e6b9.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>计算的结果会被写入到矩阵<code>roots</code>中，其包含的元素数取决于多项式实根的个数。需要注意在函数<code>cv::soleveCubic()</code>和<code>cv::sovePoly()</code>中，参数<code>coeffs</code>中元素和多项式中系数对应的方式相反，在前者中高阶系数是第一个，在后者中高阶系数是矩阵<code>coeffs</code>的最后一个元素。</p>
<h5>cv::solvePoly()</h5>
<p>该函数可以求解任意阶数的多项式实根，其原型如下。</p>
<pre><code>// maxlters：计算过程中的最大迭代数
int cv::solvePoly (cv::InputArray coeffs, cv::OutputArray roots,
                   int maxIters = 300);
</code></pre>
<p>参数<code>coeffs</code>表示的多项式如下。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1102" data-height="62"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-e5bf1bfef1a57253.png" data-original-width="1102" data-original-height="62" data-original-format="image/png" data-original-filesize="25739" src="https://upload-images.jianshu.io/upload_images/1801561-e5bf1bfef1a57253.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>和函数<code>cv::solveCubic()</code>不同的是，函数<code>cv::solvePoly()</code>会将虚根和实根一并返回。n阶多项式会包含n个根，矩阵<code>roots</code>中元素包含两个通道，基本数据类型为双精度型，双通道分别表示根的实部和虚部。</p>
<h5>cv::sort()</h5>
<p>该函数对一个二维单通道矩阵排序，其原型如下。和在微软的Excel程序中以某列或者某行排序不同，该函数会对每行或者每列单独排序。并将排序后的数据写入到一个新的矩阵dst中。</p>
<pre><code>// flags：排序策略，必须从以下两则规则中各选一个，使用逻辑与符号连接
// cv::SORT_EVERY_ROW和cv::SORT_EVERY_COLUMN分别表示对每行或者每列进行排序
// cv::SORT_ASCENDING和cv::SORT_DESCENDING分别表示升序和降序
void cv::sort(cv::InputArray src, cv::OutputArray dst, int flags);
</code></pre>
<h5>cv::sortIdx()</h5>
<p>和函数<code>cv::sort()</code>一样，该函数同样只能处理单通道的二维数组。不同的是函数<code>cv::sort()</code>是将排序后的元素写入到矩阵<code>dst</code>中，而该函数是将元素的索引写入到矩阵<code>dst</code>中。其原型如下。</p>
<pre><code>// flags：含义和函数cv::sort()中一致
void cv::sortIdx(cv::InputArray src, cv::OutputArray dst, int flags);
</code></pre>
<h5>cv::split()</h5>
<p>这类函数是函数<code>cv::mixChannels()</code>的一个简单特例。它将一个多通道矩阵分割为多个单通道矩阵。其原型如下。</p>
<pre><code>// mtx：多通道矩阵
// mv：单通道矩阵数组地址
// 数组元素的个数必须大于等于矩阵mtx的通道数
// 数组内存必须我们自己分配
void cv::split(const cv::Mat& mtx, cv::Mat* mv);

// mv：单通道矩阵向量的引用
// 该函数内部会自动为矩阵分配内存空间
void cv::split(const cv::Mat& mtx, vector<Mat>& mv);
</code></pre>
<h5>cv::sqrt()</h5>
<p>函数<code>cv::pow</code>的一个特例，该函数计算每个元素的平方根，对于多通道元素将会逐通道计算，其原型如下。</p>
<pre><code>void cv::sqrt(cv::InputArray src, cv::OutputArray dst);
</code></pre>
<p>数学中有时存在矩阵的平方根，即如果存在矩阵A和B满足关系BB = A，如果A是一个正定方阵，则B存在并只有唯一解。</p>
<p>如果A可以被对角化，则存在以A的特征向量按列组合的矩阵V使得等式 A = VDV-1成立，此处D是一个对角矩阵。由于对角矩阵的平方根等于每个元素的平方根，因此计算矩阵A的平方根可以通过如下公式计算。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="252" data-height="70"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-b56be47ddd58c452.png" data-original-width="252" data-original-height="70" data-original-format="image/png" data-original-filesize="20425" src="https://upload-images.jianshu.io/upload_images/1801561-b56be47ddd58c452.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>可以通过如下直接平方的方式来验证该等式。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="806" data-height="170"><img data-original-src="//upload-images.jianshu.io/upload_images/1801561-36e4ea757fffc3b2.png" data-original-width="806" data-original-height="170" data-original-format="image/png" data-original-filesize="79049" src="https://upload-images.jianshu.io/upload_images/1801561-36e4ea757fffc3b2.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>根据该公式写出求矩阵A的代码如下。</p>
<pre><code>void matrix_square_root(const cv::Mat& A, cv::Mat& sqrtA) &#123;
    cv::Mat U, V, Vi, E;
    cv::eigen(A, E, U);
    V = U.T();
    // 求正交矩阵V的逆，假定矩阵A是正定的，否则它的平方根将是复数
    cv::transpose(V, Vi);
    cv::sqrt(E, E);
    sqrtA = V * Mat::diag(E) * Vi;
&#125;
</code></pre>
<h5>cv::subtract()</h5>
<p>该函数简单的将两个矩阵中的元素逐个作为被减数和减数，计算它们的差，其原型如下。</p>
<pre><code>// src1和src2：被减数矩阵和减数矩阵
// mask：蒙版矩阵
// dtype：输出矩阵的基本数据类型
void cv::subtract(cv::InputArray src1, cv::InputArray  src2, cv::OutputArray dst,
                  cv::InputArray  mask  = cv::noArray(), int dtype = -1);
</code></pre>
<p>该函数可以直接使用如下的矩阵表达式替代。</p>
<pre><code>dst = src1 - src2;
dst -= src1;
</code></pre>
<h5>cv::sum()</h5>
<p>该函数用于计算矩阵中所有元素的和，它可以处理最多四通道矩阵，每个通道将会被单独求和，并将结果放到<code>cv::Scalar</code>实例中返回，其中的每个元素表示每个通道的求和结果。其原型如下。</p>
<pre><code>cv::Scalar cv::sum(cv::InputArray arr);
</code></pre>
<h5>cv::trace()</h5>
<p>该函数计算输入矩阵对角线上所有元素的和，它可以处理最多四通道的任意尺寸矩阵，每个通道将会被单独求和，并将结果放到<code>cv::Scalar</code>实例中返回，其中的每个元素表示每个通道的求和结果。其原型如下。</p>
<pre><code>cv::Scalar cv::trace(cv::InputArray  mat);
</code></pre>
<h5>cv::transform()</h5>
<p>该函数将输入矩阵内所有元素视为单个列向量，并逐个应用矩阵变换，其原型如下。矩阵mtx的尺寸为n✖️1或者n+1✖️1，n表示矩阵<code>src</code>的通道数。在第二种情况下矩阵<code>src</code>的每个元素都会被扩展值为1的一个维度。</p>
<pre><code>void cv::transform(cv::InputArray src, cv::OutputArray dst, cv::InputArray mtx);
</code></pre>
<p>这种转换的含义依赖于输入矩阵中单个元素不同通道的值的含义，如果它们的含义为颜色通道，则这种转换可以视为一种线性颜色空间转换，如在RGB和YUV颜色空间中转换。如果这些通道表示的是一个点的坐标，则这种转换可以被理解为这些点点旋转或者其他几何变换。</p>
<h5>cv::transpose()</h5>
<p>该函数用于求转置矩阵，它可以处理多通道的矩阵，但是需要记住在处理多通道矩阵时，该函数不会执行复数共轭运算。其原型如下。该函数也可以使用类<code>cv::Mat</code>的成员函数<code>cv::Mat t()</code>实现。</p>
<pre><code>void cv::transpose(cv::InputArray src, cv::OutputArray dst);
</code></pre>
<h3>3 小结</h3>
<p>矩阵对象<code>cv::Mat</code>是OpenCV中重要的数据结构，本章介绍了和其相关的大量函数。这些函数包含了从简单的线性操作到复杂的特征操作，其中部分是处理表示图像数据的矩阵，而其余部分则是处理其他类型数据的。在后面的章节中会介绍到更复杂的算法以实现复杂的计算机视觉效果，而本章的函数这是这些复杂算法的基础。</p>
  
</div>
            