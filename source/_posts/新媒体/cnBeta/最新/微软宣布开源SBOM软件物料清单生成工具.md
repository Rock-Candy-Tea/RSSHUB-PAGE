
---
title: '微软宣布开源SBOM软件物料清单生成工具'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0715/8b54ec5884202ff.png'
author: cnBeta
comments: false
date: Fri, 15 Jul 2022 09:55:41 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0715/8b54ec5884202ff.png'
---

<div>   
在周二的一篇开发者博客中，微软 One Engineering System（1ES）产品主管 Danesh Kumar Badlani 与 1ES 首席项目主管 Adrian Diglio 隆重宣布了 Salus 软件物料清单（SBOM）生成工具的已经走向开源。<strong>据悉，作为响应改善国家网络安全的一道行政命令的最新举措，其有助于组织机构建立起对其供应链依赖关系的洞察力。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0715/8b54ec5884202ff.png" alt="0.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">截图（来自：<a href="https://devblogs.microsoft.com/engineering-at-microsoft/microsoft-open-sources-salus-software-bill-of-materials-sbom-generation-tool/" target="_self">GitHub</a>）</p><p>作为一款通用的、经过企业验证、构建时（build-time）的 SBOM 生成器，SBOM 适用于包括 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>、Linux 和 Mac 在内的平台，并且采用了标准的软件包数据交换（SPDX）格式。</p><p>Salus 能够轻松集成到软件的构建工作流程中，并通过组件自动检测 NPM、NuGet、PyPI、CocoaPods、Maven、Golang、Rust Crates、RubyGems、容器内的 Linux 包、Gradle、Ivy、以及 GitHub 等公共平台上的存储。</p><p>随着时间的推移，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>还会持续改进 SBOM 工具、并添加更多的检测组件。</p><p><img src="https://static.cnbetacdn.com/article/2022/0715/84cf124cf2ea616.png" alt="1.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">分层构建流程示意图</p><p>Salus 生成的 SBOM，包含了基于 SPDX 规范的四个主要部分。</p><blockquote><p>● 文档创建信息：例如软件名称、SPDX 版本 / 许可证、文档创建者、创建时间等。</p><p>● 文件部分：组成软件的文件列表，每个文件都包含有一些属性、以及 SHA-1 / SHA-256 内容哈希值。</p><p>● 包部分：构建软件时使用的包列表，每个包都具有名称、版本、供应商、哈希值、包 URL（purl）、软件标识符等属性。</p><p>● 关系部分：SBOM 不同元素之间的关系列表，比如文件和包。</p></blockquote><p>值得一提的是，Salus 还可参考其他 SBOM 文档来捕获完整的依赖关系树。</p><p><img src="https://static.cnbetacdn.com/article/2022/0715/9cb07305c306f51.png" alt="2.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">Document Creation Information 示例代码</p><p>最后，微软希望能够通过与开源社区的通力协作，帮助所有人都能够遵循行政命令的指导。</p><p>开源 Salus 是该公司在社区内促进协作和创新的重要一步，且微软相信这可使更多组织能够受益于 SBOM、并为后续的长期发展做出积极的贡献。</p>   
</div>
            