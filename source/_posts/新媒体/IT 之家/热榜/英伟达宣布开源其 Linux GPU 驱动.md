
---
title: '英伟达宣布开源其 Linux GPU 驱动'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2022/5/c4211019-018f-4968-843f-2fff8847bc89.png'
author: IT 之家
comments: false
date: Thu, 12 May 2022 04:07:07 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/5/c4211019-018f-4968-843f-2fff8847bc89.png'
---

<div>   
<div class="tougao-user">感谢IT之家网友 <a href="https://m.ithome.com/html/app/open.html?url=ithome%3A%2F%2Fuserpage%3Fid%3D2056699" rel="nofollow">OC_Formula</a>、<a href="https://m.ithome.com/html/app/open.html?url=ithome%3A%2F%2Fuserpage%3Fid%3D1072583" rel="nofollow">外乡人_</a>、<a href="https://m.ithome.com/html/app/open.html?url=ithome%3A%2F%2Fuserpage%3Fid%3D1753279" rel="nofollow">软媒用户1753279</a>、<a href="https://m.ithome.com/html/app/open.html?url=ithome%3A%2F%2Fuserpage%3Fid%3D1556690" rel="nofollow">生之如舟</a>、<a href="https://m.ithome.com/html/app/open.html?url=ithome%3A%2F%2Fuserpage%3Fid%3D420138" rel="nofollow">久居大大</a>、<a href="https://m.ithome.com/html/app/open.html?url=ithome%3A%2F%2Fuserpage%3Fid%3D1355951" rel="nofollow">飞羽zoxoy</a>、<a href="https://m.ithome.com/html/app/open.html?url=ithome%3A%2F%2Fuserpage%3Fid%3D1407324" rel="nofollow">风烨晨曦</a>、<a href="https://m.ithome.com/html/app/open.html?url=ithome%3A%2F%2Fuserpage%3Fid%3D1012448" rel="nofollow">imisaka</a>、<a href="https://m.ithome.com/html/app/open.html?url=ithome%3A%2F%2Fuserpage%3Fid%3D1911896" rel="nofollow">诺基亚X_</a>、<a href="https://m.ithome.com/html/app/open.html?url=ithome%3A%2F%2Fuserpage%3Fid%3D1546155" rel="nofollow">这个昵称不怎么样</a>、<a href="https://m.ithome.com/html/app/open.html?url=ithome%3A%2F%2Fuserpage%3Fid%3D1910348" rel="nofollow">软媒新友1910348</a>、<a href="https://m.ithome.com/html/app/open.html?url=ithome%3A%2F%2Fuserpage%3Fid%3D1679115" rel="nofollow">ShiraYuki</a> 的线索投递！</div>
            <p data-vmark="c1f0"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 5 月 12 日消息，英伟达宣布从 R515 版驱动程序开始将以开源的形式发布其 Linux GPU 内核驱动，此开源还将具有 GPL 和 MIT 双重许可证。</p><p data-vmark="fd1b" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/5/c4211019-018f-4968-843f-2fff8847bc89.png" w="594" h="330" alt="图片 5" title="英伟达宣布开源其 Linux GPU 驱动" width="594" height="330" referrerpolicy="no-referrer"></p><p data-vmark="7706">此次开源将改善在 Linux 系统中使用英伟达 GPU 的体验，<span class="accentTextColor">其能使硬件和系统之间的联系更为紧密，并且能够让开发人员进行调试、整合和回馈</span>。此举也能够让软件发行商更容易将驱动程序打包在他们的软件之中。</p><p data-vmark="5f9d">英伟达此次开源驱动的主要目标之一为改善其 GPU 对大型数据中心和超级计算机的功能和支持。因为超级计算机都是使用定制的 Linux 系统，闭源的驱动程序不方便其 GPU 进行安装和维护。</p><p data-vmark="d244" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/5/2b90a62a-0f29-4e19-9a32-57e486a54fc6.png" w="580" h="318" alt="图片 4" title="英伟达宣布开源其 Linux GPU 驱动" width="580" height="318" referrerpolicy="no-referrer"></p><p data-vmark="1a36">英伟达表示：在过去一年分阶段推出 GSP 驱动架构（图灵和安培架构的默认配置）后，源代码已经能用在图灵（20 系显卡架构）和安培（30 系显卡架构）架构的计算卡上了。而且源代码已经在各种工作负载中进行了测试，以确保其性能和功能能够与驱动程序能保持一致。但源代码也带来了新的功能，如用于跨设备以及子系统共享缓存的 DMA-BUF 框架，该框架将在 Hopper 架构（英伟达最新的 H100 计算卡就是该架构）中发挥其作用。而使用图灵架构以前的 GPU 的用户则只能继续使用旧版驱动。</p><p data-vmark="75cb" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/5/1c0abfd4-00a7-4344-87b2-c1d85c3cc5d5.png" w="613" h="335" alt="图片 2" title="英伟达宣布开源其 Linux GPU 驱动" width="613" height="335" referrerpolicy="no-referrer"></p><p data-vmark="8bec" style="text-align: center;">（H100 GPU）</p><p data-vmark="53cb">开源版驱动程序和以前的程序可以使用相同的固件，其用户模式堆栈也同样是 CUDA、OpenGL 和 Vulkan，区别仅为唯一的规定是驱动程序堆栈的所有组件必须与发行版中的版本匹配。社区提交的补丁将考虑集成到未来版本的驱动程序中。</p><p data-vmark="50dd">英伟达还透露，它正在与 Linux 内核社区和合作伙伴合作开发上游方法，因为它目前的代码库不符合 Linux 设计规范，它也不是 Linux 上游的候选者。此外，源代码还将用于改进开源 Nouveau 驱动程序。</p>
          
</div>
            