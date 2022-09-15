
---
title: 'Img2img 图像合成算法AI把老游戏的图形优化成细节丰富的样子'
categories: 
 - 图片
 - 煎蛋
 - 首页
headimg: 'https://cors.zfour.workers.dev/?http://img.jandan.net/news/2018/09/7b50a4e1e7245c57fc5e29a982c96792.jpg!custom'
author: 煎蛋
comments: false
date: Tue, 13 Sep 2022 15:02:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://img.jandan.net/news/2018/09/7b50a4e1e7245c57fc5e29a982c96792.jpg!custom'
---

<div>   
<blockquote><p>分享一个AI资源</p></blockquote><img src="https://cors.zfour.workers.dev/?http://img.jandan.net/news/2018/09/7b50a4e1e7245c57fc5e29a982c96792.jpg!custom" referrerpolicy="no-referrer"><p>大上周，Reddit上名为 frigis9 的用户发布了6张图片，其中包含对经典 MS-DOS 计算机游戏的图形优化，有《Commander Keen 6》和《猴岛的秘密》中的画面。最有趣的部分是他是如何做到的：使用被称为“img2img”(图像到图像)的图像合成技术。该技术先获取输入图像，应用书面文本提示，生成类似的输出图像作为结果。→<a href="https://cdn.arstechnica.net/wp-content/uploads/2022/09/ms_dos_game_upgrade_set.jpg">https://cdn.arstechnica.net/wp-content/uploads/2022/09/ms_dos_game_upgrade_set.jpg</a></p>
<p>这是稳定扩散图像合成模型(Stable Diffusion image synthesis model )新发布的功能。Stable Diffusion 的一大优势是能运行在单张显卡上，包括苹果的 M1 Mac GPU，因此用户可在本地运行。</p>
<p>在和其他用户交流时，frigis9 提供了更多关于如何使用名为 Visions of Chaos 的前端程序制作图像的详细信息，后者是多功能应用程序，可以生成许多不同风格的计算机合成艺术品：“像这样的简单肖像，将初始图像强度设置为0.25。对于较暗、细节较少的图像，可能必须将其提高到 0.35 或 0.4。只需要摆弄图像强度值，一旦你找对路子了(即你的输出图像多少看起来像初始输入图像了)，在提示下添加或删除细节。调整，冲洗并重复大约一百次，直到你得到完美的(嗯，足够好)图像。”</p>
<p>在过去的数周里，Stable Diffusion的 img2img 功能的用户优化了儿童绘画，将涂鸦变成了沙漠中闪闪发光的骑士，升级了他们的头像等等。目前，在个人机器上运行img2img仍然是一个技术性的过程，但通过使用 Visions of Chaos 和 Hugging Face 上的模型等图形前端，大家可以自己试验。技术还在迅速发展，因此更好的交互应用已指日可待。</p>
<p>图像合成结果的质量，目前需要大量的试验和精心的挑选，才能实现frigis9发布的效果——可能需要数小时的工作。但是随着图像合成技术和GPU能力的进步，我们可以预期，未来的图形优化技术可以把老像素游戏的画面变得更加丰富细腻。</p>
<p>https://arstechnica.com/gaming/2022/09/pixel-art-comes-to-life-fan-upgrades-classic-ms-dos-games-with-ai/</p>
<p>就如正文所说，新发布的Stable Diffusion可以在本地运行。</p>
<p>微博用户@分形_噪波 制作的<a href="https://www.bilibili.com/read/cv18495050">简易教程</a>，以及提供的 <a href="https://pan.baidu.com/s/1pB9iwdD43DyL-phYUJqBHQ?pwd=qh42">本地网盘版下载链接</a>。文件有8G。</p>
<p>如果需要原汁原味的官方版，可以从<a href="https://github.com/sd-webui/stable-diffusion-webui">GitHub下载</a>。但原版需要配置环境变量。</p>
<p>网盘版把模型和环境文件都配置好了，只需要安装miniconda然后把相应文件夹按照步骤放置到相应位置就可以较简单地配置完环境使用。</p>
<p>详细步骤：</p>
<h4 class="pullquote">1.安装miniconda3，安装中勾选为所有用户安装，建议装在默认路径不要改<br>
2.把ldo文件复制到安装目录的envs文件夹中，默认路径是C:ProgramDataMiniconda3envs<br>
3.在一个空间富裕的盘新建一个文件夹，将stable-diffusion文件夹复制进去<br>
4.找到文件夹中的webui.cmd文件，右键编辑，将第四行的set cutom_conda_path=后面改成minicoda的安装目录，默认是cutom_conda_path=C:ProgramDataMiniconda3，保存<br>
5.运行webui.cmd文件 耐心等待 中间报错的话尝试关闭梯子或打开梯子，反复尝试<br>
6.最终命令行中会出现一个地址，复制到浏览器中就可以使用了</h4>  
</div>
            