
---
title: '一行代码消除 PyTorch 的 CUDA 内存溢出报错，这个 GitHub 项目刚发布就揽星 600+'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2021/12/e39c0cbb-e829-423c-a842-6599341f2306.png'
author: IT 之家
comments: false
date: Sat, 18 Dec 2021 14:15:44 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/12/e39c0cbb-e829-423c-a842-6599341f2306.png'
---

<div>   
<p data-vmark="7321">多少人用 PyTorch“炼丹”时都会被这个 bug 困扰。</p><pre class="brush:javascript;toolbar:false">CUDA error: out of memory.</pre><p data-vmark="1868"><img src="https://img.ithome.com/newsuploadfiles/2021/12/e39c0cbb-e829-423c-a842-6599341f2306.png" w="1080" h="235" alt="代码截图" title="一行代码消除 PyTorch 的 CUDA 内存溢出报错，这个 GitHub 项目刚发布就揽星 600+" width="1080" height="178" referrerpolicy="no-referrer"></p><p data-vmark="e2f7">一般情况下，你得找出当下占显存的没用的程序，然后 kill 掉。如果不行，还需手动调整 batch size 到合适的大小，有点麻烦。</p><p data-vmark="82e8">现在，有人写了一个 PyTorch wrapper，<span class="accentTextColor">用一行代码就能“无痛”消除这个 bug</span>。</p><p data-vmark="faf1"><img src="https://img.ithome.com/newsuploadfiles/2021/12/daa3c8ae-d35e-44bb-bff1-71daa5f06b62.gif" w="400" h="225" alt="图片" title="一行代码消除 PyTorch 的 CUDA 内存溢出报错，这个 GitHub 项目刚发布就揽星 600+" width="400" height="225" referrerpolicy="no-referrer"></p><p data-vmark="f32b">有多厉害？</p><p data-vmark="57e0">相关项目在 GitHub 才发布没几天就收获了 600 + 星。</p><p data-vmark="ee46"><img src="https://img.ithome.com/newsuploadfiles/2021/12/418a5305-ee7f-485c-98e1-4e4e74ce53fb.png" w="806" h="232" alt="图片" title="一行代码消除 PyTorch 的 CUDA 内存溢出报错，这个 GitHub 项目刚发布就揽星 600+" width="806" height="232" referrerpolicy="no-referrer"></p><h2 data-vmark="d023">一行代码解决内存溢出错误</h2><p data-vmark="f0e4">软件包名叫 koila，已经上传 PyPI，先安装一下：</p><pre class="brush:javascript;toolbar:false ai-word-checked">pip install koila</pre><p data-vmark="fcba">现在，假如你面对这样一个 PyTorch 项目：构建一个神经网络来对 FashionMNIST 数据集中的图像进行分类。</p><p data-vmark="b412">先定义 input、label 和 model：</p><pre class="brush:javascript;toolbar:false"># A batch of MNIST image
input = torch.randn(8, 28, 28)
# A batch of labels
label = torch.randn(0, 10, [8])
class NeuralNetwork(Module):
def __init__(self):
super(NeuralNetwork, self).__init__()
self.flatten = Flatten()
self.linear_relu_stack = Sequential(
Linear(28 * 28, 512),
ReLU(),
Linear(512, 512),
ReLU(),
Linear(512, 10),
)
def forward(self, x):
x = self.flatten(x)
logits = self.linear_relu_stack(x)
return logits</pre><p data-vmark="cfac">然后定义 loss 函数、计算输出和 losses。</p><pre class="brush:javascript;toolbar:false ai-word-checked">loss_fn = CrossEntropyLoss()
# Calculate losses
out = nn(t)
loss = loss_fn(out, label)
# Backward pass
nn.zero_grad()
loss.backward()</pre><p data-vmark="5cf2">好了，如何使用 koila 来防止内存溢出？</p><p data-vmark="503a">超级简单！</p><p data-vmark="8e59">只需在第一行代码，<span class="accentTextColor">也就是把输入用 lazy 张量 wrap 起来，并指定 bacth 维度</span>，koila 就能自动帮你计算剩余的 GPU 内存并使用正确的 batch size 了。</p><p data-vmark="3bcb">在本例中，batch=0，则修改如下：</p><pre class="brush:javascript;toolbar:false">input = lazy(torch.randn(8, 28, 28), batch=0)</pre><p data-vmark="1c9e">完事儿！就这样和 PyTorch“炼丹”时的 OOM 报错说拜拜。</p><h2 data-vmark="f196">灵感来自 TensorFlow 的静态 / 懒惰评估</h2><p data-vmark="e042">下面就来说说 koila 背后的工作原理。</p><p data-vmark="10c0">“CUDA error: out of memory”这个报错通常发生在前向传递（forward pass）中，因为这时需要保存很多临时变量。</p><p data-vmark="4e32">koila 的灵感来自 TensorFlow 的静态 / 懒惰评估（static / lazy evaluation）。</p><p data-vmark="24e3">它通过构建图，并仅在必要时运行访问所有相关信息，来确定模型真正需要多少资源。</p><p data-vmark="93ac">而只需计算临时变量的 shape 就能计算各变量的内存使用情况；而知道了在前向传递中使用了多少内存，koila 也就能自动选择最佳 batch size 了。</p><p data-vmark="c93d">又是算 shape 又是算内存的，koila 听起来就很慢？</p><p data-vmark="b34b"><img src="https://img.ithome.com/newsuploadfiles/2021/12/d27961fc-5e9d-437f-8e5e-e6b6694aa918.png" w="500" h="500" alt="图片" title="一行代码消除 PyTorch 的 CUDA 内存溢出报错，这个 GitHub 项目刚发布就揽星 600+" width="500" height="500" referrerpolicy="no-referrer"></p><p data-vmark="9faf">NO。</p><p data-vmark="4fa5">即使是像 GPT-3 这种具有 96 层的巨大模型，其计算图中也只有几百个节点。</p><p data-vmark="0ca1">而 Koila 的算法是在线性时间内运行，任何现代计算机都能够立即处理这样的图计算；再加上大部分计算都是单个张量，所以，koila 运行起来一点也不慢。</p><p data-vmark="c9e9">你又会问了，PyTorch Lightning 的 batch size 搜索功能不是也可以解决这个问题吗？</p><p data-vmark="8bfe">是的，它也可以。</p><p data-vmark="2b09">但作者表示，该功能已深度集成在自己那一套生态系统中，你必须得用它的 DataLoader，从他们的模型中继承子类，才能训练自己的模型，太麻烦了。</p><p data-vmark="a7ab">而 koila 灵活又轻量，只需一行代码就能解决问题，非常“大快人心”有没有。</p><p data-vmark="a25a">不过目前，koila 还不适用于分布式数据的并行训练方法（DDP），未来才会支持多 GPU。</p><p data-vmark="f710">以及现在只适用于常见的 nn.Module 类。</p><p data-vmark="c394"><img src="https://img.ithome.com/newsuploadfiles/2021/12/ad15afc3-986e-4160-8393-ea3379379c22.png" w="1080" h="178" alt="图片" title="一行代码消除 PyTorch 的 CUDA 内存溢出报错，这个 GitHub 项目刚发布就揽星 600+" width="1080" height="135" referrerpolicy="no-referrer"></p><p data-vmark="c0ec">ps：koila 作者是一位叫做 RenChu Wang 的小哥。</p><p data-vmark="fe88"><img src="https://img.ithome.com/newsuploadfiles/2021/12/366ae572-f069-424c-a7d8-03997d910f59.png" w="574" h="832" alt="图片" title="一行代码消除 PyTorch 的 CUDA 内存溢出报错，这个 GitHub 项目刚发布就揽星 600+" width="574" height="832" referrerpolicy="no-referrer"></p><p data-vmark="0045">项目地址：<a href="https://github.com/rentruewang/koila" target="_blank">点此直达</a></p><p data-vmark="e2d6">参考链接：<a href="https://www.reddit.com/r/MachineLearning/comments/r4zaut/p_eliminate_pytorchs_cuda_error_out_of_memory/" target="_blank">点此直达</a></p>
          
</div>
            