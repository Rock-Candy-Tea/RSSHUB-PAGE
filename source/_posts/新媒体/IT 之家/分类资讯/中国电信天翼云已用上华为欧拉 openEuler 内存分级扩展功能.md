
---
title: '中国电信天翼云已用上华为欧拉 openEuler 内存分级扩展功能'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2021/11/5ebd5dbf-2184-4fff-a0ee-812f2e222711.png'
author: IT 之家
comments: false
date: Tue, 09 Nov 2021 08:58:08 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/11/5ebd5dbf-2184-4fff-a0ee-812f2e222711.png'
---

<div>   
<p data-vmark="a4db"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 11 月 9 日消息，据 openEuler 发布，近期，天翼云和华为 openEuler 开源团队就内存分级扩展功能进行了联合创新，并在天翼云虚拟化场景进行了内部原型验证，测试结果表现，内存分级技术极大提升了内存性价比。</p><p data-vmark="68ba"><strong>背景</strong></p><p data-vmark="3ff4">受制于内存工艺瓶颈，内存成本高；随着 CPU 算力的发展，尤其是 ARM 核成本的降低，内存成为约束业务成本和性能的关键问题。如何节省内存成本、扩大内存容量成为迫切需要解决的问题。因此，openEuler 推出了内存分级扩展功能。</p><p data-vmark="bf58">内存分级扩展功能在不影响业务功能情况下，通过 DRAM 和低速内存介质，如 SCM、AEP 等形成多级内存，通过内存自动调度让热数据在 DRAM 高速内存区中运行，让冷数据交换到低速内存区，从而增加内存容量，保证核心业务高效平稳运行。该特性适用于内存使用量大，且使用相对不频繁的应用进程上，在这些场景中的效果较好，收益较大。</p><p data-vmark="02c4"><strong>联创成果</strong></p><p data-vmark="d1b2">在虚拟化场景下，如何扩大内存容量的同时降低内存成本，提升内存超售比，是天翼云面临的业务痛点。针对该痛点，天翼云和华为 openEuler 开源团队决定在虚拟机内部业务访问不频繁的场景中验证内存分级技术，尝试提升虚拟机密度，同时保持业务性能持平或少量下降。</p><p data-vmark="d611">通过联合创新，对 AEP 搭配 DDR 场景进行了原型验证，开启内存扩展功能相比未开启时，AEP 中虚拟机的 redis 性能提高了约 30%，基本达到与 DDR 中虚拟机 redis 性能一致的水平。同时，等内存容量下，使用 DDR 搭配 AEP 比纯 DDR 场景，内存成本下降了约 35%，显著提升了内存使用的性价比。</p><p data-vmark="1560"><img src="https://img.ithome.com/newsuploadfiles/2021/11/5ebd5dbf-2184-4fff-a0ee-812f2e222711.png" w="554" h="313" title="中国电信天翼云已用上华为欧拉 openEuler 内存分级扩展功能" width="554" height="313" referrerpolicy="no-referrer"></p><p data-vmark="3580"><img src="https://img.ithome.com/newsuploadfiles/2021/11/eb89d3af-2610-4166-b023-0a3ae1b1a38c.png" w="554" h="311" title="中国电信天翼云已用上华为欧拉 openEuler 内存分级扩展功能" width="554" height="311" referrerpolicy="no-referrer"></p><p data-vmark="bbd6"><img src="https://img.ithome.com/newsuploadfiles/2021/11/3625d779-4f39-4b23-9d83-3f8516c60996.png" w="554" h="311" title="中国电信天翼云已用上华为欧拉 openEuler 内存分级扩展功能" width="554" height="311" referrerpolicy="no-referrer"></p>
          
</div>
            