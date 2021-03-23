
---
title: '大话 Block 层：数据单元'
categories: 
 - 博客
 - 阿里云系统组技术博客
 - — 首页
headimg: 'https://kernel.taobao.org//2020/08/Block_Story_Data_Unit/IO_stack.jpg'
author: 阿里云系统组技术博客
comments: false
date: Fri, 14 Aug 2020 00:00:00 GMT
thumbnail: 'https://kernel.taobao.org//2020/08/Block_Story_Data_Unit/IO_stack.jpg'
---

<div>   
<p>本文介绍 IO 栈中的各种数据单元。</p> <h2 id="io-stack">IO Stack</h2> <p><img src="https://kernel.taobao.org//2020/08/Block_Story_Data_Unit/IO_stack.jpg" alt="IO_stack" referrerpolicy="no-referrer"></p> <h2 id="data-unit">Data Unit</h2> <p>IO 栈的不同层次使用不同的数据存储单元来抽象 block 设备的地址空间</p> <h3 id="sector">sector</h3> <p>块设备通常不能按照字节寻址，HDD 的寻址单元是扇区 (sector)，扇区的大小是 512 字节</p> <p>由于早期的 block layer 都是为 HDD 设计，因而就使用 sector 的概念描述块设备的寻址单元；即使之后出现的 NAND flash 其寻址单元可能是 512/2k/4k 字节，但是 sector 的概念一直沿用至今，并一直保持为 512 字节</p> <p>如今 sector 其实是 block layer 软件层的概念，sector 的大小固定为 512 bytes</p> <p><img src="https://kernel.taobao.org//2020/08/Block_Story_Data_Unit/block_data_units_sector.jpg" alt="block_data_units_sector-c200" referrerpolicy="no-referrer"></p> <h3 id="block">block</h3> <p>文件系统使用 block 对块设备的地址空间进行寻址，block 的大小是文件系统初始化的时候配置的，例如 mkfs.ext4 的时候可以配置 ext4 文件系统的 block size，ext4 中 block size 可以在 1K ~ 64K 范围内以 2 倍递增，因而一个 block 可以包含多个 sector</p> <p><img src="https://kernel.taobao.org//2020/08/Block_Story_Data_Unit/block_data_units_block.jpg" alt="block_data_units_block-c200" referrerpolicy="no-referrer"></p> <p>文件系统会使用内存对磁盘上的 block 进行缓存，这一部分用于缓存 block 的内存就称为 block buffer</p> <p>block size 不能超过 page frame size，否则就无法使用 block buffer 特性</p> <p>以下描述内存中的 block buffer 与磁盘上的 block 之间的映射关系</p> <ul> <li>如果 page frame size == block size，那么一个 page frame 中只能容纳一个 block buffer，此时一个 page frame 只能缓存一个 block</li> <li>如果 page frame size > block size，那么一个 page frame 中可以容纳多个 block buffer，一个 page frame 中缓存的多个 block 不一定连续</li> </ul> <p><img src="https://kernel.taobao.org//2020/08/Block_Story_Data_Unit/block_data_units_block_buffer.jpg" alt="block_data_units_block_buffer-c400" referrerpolicy="no-referrer"></p> <h3 id="segment">segment</h3> <p>hardware disk controller 和 block device driver 还有 segment 的概念</p> <p>segment 的概念实际来自 DMA controller，DMA 中使用 segment 的概念描述一段连续的物理内存区间，支持 scatter-gather 特性的 DMA controller 可以在一次 DMA transfer 中，实现一个或多个 segment (discontinuous physical memory) 和一段连续的设备物理地址区间 (adjacent disk sectors) 之间的数据传输，此时一次 scatter-gather DMA transfer 实际上就包含一个或多个 segment</p> <p><img src="https://kernel.taobao.org//2020/08/Block_Story_Data_Unit/DMA_scatter_gather.jpg" alt="DMA_scatter_gather" referrerpolicy="no-referrer"></p> <p>segment 可以是一个 page，也可以是一个 page 的其中一部分，也可以包含多个 page，通常存储一个或多个相邻的 sector 的数据</p> <p><img src="https://kernel.taobao.org//2020/08/Block_Story_Data_Unit/block_data_units_segment.jpg" alt="block_data_units_segment-c400" referrerpolicy="no-referrer"></p>   
</div>
            