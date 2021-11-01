
---
title: 'OpenVDB 9.0.0 发布，梦工厂开源的视觉效果工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7879'
author: 开源中国
comments: false
date: Mon, 01 Nov 2021 07:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7879'
---

<div>   
<div class="content">
                                                                                            <p>OpenVDB 是一个用于视觉效果和动画的开源 C++ 库和工具，由知名动画公司梦工厂所开发并在 MPL 2.0 协议下分发，现在由 ASWF 负责维护。该工具曾被用于制作《星球大战》、《疯狂原始人》、《冰雪奇缘》和《驯龙高手》等作品。</p> 
<p><strong>OpenVDB 9.0.0 中值得关注的内容包括：</strong></p> 
<ul> 
 <li>NanoVDB 正式推出，首次为 OpenVDB 的静态稀疏卷积提供 GPU 支持；</li> 
 <li>支持显式模板实例化，加快了下游构建时间，大多数工具都默认启用；</li> 
 <li>增加了对 OpenEXR 3 和 TBB 2021 的支持；</li> 
 <li>为 RootNode、InternalNode 和 LeafNode 增加了瞬态数据；</li> 
 <li>增加了 <code>tools::countActiveLeafVoxels()</code>、 <code>tools::countInactiveVoxels()</code>、 <code>tools::countInactiveLeafVoxels()</code> 和 <code>tools::activeTiles()</code> 来执行多线程计数；</li> 
 <li>增加了 <code>hsvtogrb()</code>和 <code>rgbtohsv()</code> AX 辅助函数，用于将色调、饱和度和数值输入转换为 RGB 值，反之亦然；</li> 
 <li>为 OpenVDB AX 增加了一个 Python 绑定，允许你从 Python 模块调用加速的 AX 代码；</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAcademySoftwareFoundation%2Fopenvdb%2Freleases%2Ftag%2Fv9.0.0" target="_blank">https://github.com/AcademySoftwareFoundation/openvdb/releases/tag/v9.0.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            