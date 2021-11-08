
---
title: '为什么 Windows 文件设计成占用无法删除？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://pic4.zhimg.com/v2-8a8085344d537f34f20b8e58235a3e8b_1440w.jpg'
author: 知乎
comments: false
date: Mon, 08 Nov 2021 03:42:35 GMT
thumbnail: 'https://pic4.zhimg.com/v2-8a8085344d537f34f20b8e58235a3e8b_1440w.jpg'
---

<div>   
北极的回答<br><br><p>要回答这个问题，先要分析一下：<b>如何让文件系统允许删除正在打开的文件？</b></p><p>这个问题看上去简单，其实设计起来比较复杂的。比如，在Linux上删除正在打开的文件，那么打开的文件FD是仍然可用的，文件的全部内容都是可见的，直到最后一个FD关闭了为止（引用计数为0）。文件系统只是把对应的文件设成“待删除”的状态，等待引用计数归零以后才真正在后台删除。这期间，“待删除”文件仍然占用着磁盘空间。这需要文件系统和操作系统支持：</p><p><b>1. 在内存中维护一个待删除的队列</b></p><p>为什么不在硬盘上？理论上可以在硬盘上，但会增大文件系统设计的复杂度。这跟FAT的文件名删除标记是不同的，待删除的文件，整个数据结构在磁盘上都是存在的，只有名字不存在。而FAT的文件名删除标记打上以后，FAT链表也会跟着释放掉。</p><p><b>2. 文件系统内部有一个清理任务（线程？）去完成真正的删除动作</b></p><p>这个比较容易理解，就是有个任务专门负责清理待删除文件。</p><p><b>3. 操作系统的cache管理能针对一个删除的名字（甚至是重名）文件做管理，并正确区分。</b></p><p>比如，现在有1.txt文件正在被使用，然后被删掉了，又创建了1.txt文件，又被打开了，那么此时操作系统内部，以文件名作为索引的话，是有两个1.txt文件的，一个是被删除的状态，但文件内容，以及对应的cache块都是存在的。这个看上去比较简单的事情，才是最麻烦的，要操作系统的cache管理层负责维护两个重名文件，而cache管理又往往是操作系统最核心的部分。</p><hr><p>现在来看Windows的实现，虽然Windows提供了FILE_SHARE_DELETE，但是如果看一下WRK的代码就知道了，这个玩意仅仅只是打了个标记，根本不涉及任何内核上限制性的内容，所以这个flag不能解释任何原因。</p><p>有兴趣的可以看一下IoCheckShareAccess的实现：</p><a href="http://link.zhihu.com/?target=https%3A//github.com/HighSchoolSoftwareClub/Windows-Research-Kernel-WRK-/blob/master/WRK-v1.2/base/ntos/io/iomgr/iosubs.c%23L3178" data-draft-node="block" data-draft-type="link-card" class=" external" target="_blank" rel="nofollow noreferrer"><span class="invisible">https://</span><span class="visible">github.com/HighSchoolSo</span><span class="invisible">ftwareClub/Windows-Research-Kernel-WRK-/blob/master/WRK-v1.2/base/ntos/io/iomgr/iosubs.c#L3178</span><span class="ellipsis"></span></a><p>那么Windows不能这么做的原因，只能到文件系统驱动里去找，微软开源了FAT的驱动源码（FASTFAT）通过对比WRK源码可以发现，Windows内核标记一个文件对象的，是一个叫FILE_OBJECT的数据结构：</p><div class="highlight"><pre><code class="language-c"><span><span class="k">typedef</span> <span class="k">struct</span> <span class="n">_FILE_OBJECT</span> <span class="p">&#123;</span>
    <span class="n">CSHORT</span> <span class="n">Type</span><span class="p">;</span>
    <span class="n">CSHORT</span> <span class="n">Size</span><span class="p">;</span>
    <span class="n">PDEVICE_OBJECT</span> <span class="n">DeviceObject</span><span class="p">;</span>
    <span class="n">PVPB</span> <span class="n">Vpb</span><span class="p">;</span>
    <span class="n">PVOID</span> <span class="n">FsContext</span><span class="p">;</span>
    <span class="n">PVOID</span> <span class="n">FsContext2</span><span class="p">;</span>
    <span class="n">PSECTION_OBJECT_POINTERS</span> <span class="n">SectionObjectPointer</span><span class="p">;</span>
    <span class="n">PVOID</span> <span class="n">PrivateCacheMap</span><span class="p">;</span>
    <span class="n">NTSTATUS</span> <span class="n">FinalStatus</span><span class="p">;</span>
    <span class="k">struct</span> <span class="n">_FILE_OBJECT</span> <span class="o">*</span><span class="n">RelatedFileObject</span><span class="p">;</span>
    <span class="n">BOOLEAN</span> <span class="n">LockOperation</span><span class="p">;</span>
    <span class="n">BOOLEAN</span> <span class="n">DeletePending</span><span class="p">;</span>
    <span class="n">BOOLEAN</span> <span class="n">ReadAccess</span><span class="p">;</span>
    <span class="n">BOOLEAN</span> <span class="n">WriteAccess</span><span class="p">;</span>
    <span class="n">BOOLEAN</span> <span class="n">DeleteAccess</span><span class="p">;</span>
    <span class="n">BOOLEAN</span> <span class="n">SharedRead</span><span class="p">;</span>
    <span class="n">BOOLEAN</span> <span class="n">SharedWrite</span><span class="p">;</span>
    <span class="n">BOOLEAN</span> <span class="n">SharedDelete</span><span class="p">;</span>
    <span class="n">ULONG</span> <span class="n">Flags</span><span class="p">;</span>
    <span class="n">UNICODE_STRING</span> <span class="n">FileName</span><span class="p">;</span>
    <span class="n">LARGE_INTEGER</span> <span class="n">CurrentByteOffset</span><span class="p">;</span>
    <span class="n">ULONG</span> <span class="n">Waiters</span><span class="p">;</span>
    <span class="n">ULONG</span> <span class="n">Busy</span><span class="p">;</span>
    <span class="n">PVOID</span> <span class="n">LastLock</span><span class="p">;</span>
    <span class="n">KEVENT</span> <span class="n">Lock</span><span class="p">;</span>
    <span class="n">KEVENT</span> <span class="n">Event</span><span class="p">;</span>
    <span class="n">PIO_COMPLETION_CONTEXT</span> <span class="n">CompletionContext</span><span class="p">;</span>
<span class="p">&#125;</span> <span class="n">FILE_OBJECT</span><span class="p">;</span>
</span></code></pre></div><a href="http://link.zhihu.com/?target=https%3A//github.com/HighSchoolSoftwareClub/Windows-Research-Kernel-WRK-/blob/master/WRK-v1.2/base/ntos/inc/io.h%23L1791" data-draft-node="block" data-draft-type="link-card" class=" external" target="_blank" rel="nofollow noreferrer"><span class="invisible">https://</span><span class="visible">github.com/HighSchoolSo</span><span class="invisible">ftwareClub/Windows-Research-Kernel-WRK-/blob/master/WRK-v1.2/base/ntos/inc/io.h#L1791</span><span class="ellipsis"></span></a><p>对于Linux来说是一个叫file的数据结构</p><div class="highlight"><pre><code class="language-c"><span><span class="k">struct</span> <span class="n">file</span> <span class="p">&#123;</span>
<span class="k">union</span> <span class="p">&#123;</span>
<span class="k">struct</span> <span class="n">llist_node</span><span class="n">fu_llist</span><span class="p">;</span>
<span class="k">struct</span> <span class="n">rcu_head</span> <span class="n">fu_rcuhead</span><span class="p">;</span>
<span class="p">&#125;</span> <span class="n">f_u</span><span class="p">;</span>
<span class="k">struct</span> <span class="n">path</span><span class="n">f_path</span><span class="p">;</span>
<span class="k">struct</span> <span class="n">inode</span><span class="o">*</span><span class="n">f_inode</span><span class="p">;</span><span class="cm">/* cached value */</span>
<span class="k">const</span> <span class="k">struct</span> <span class="n">file_operations</span><span class="o">*</span><span class="n">f_op</span><span class="p">;</span>

<span class="cm">/*</span>
<span class="cm"> * Protects f_ep, f_flags.</span>
<span class="cm"> * Must not be taken from IRQ context.</span>
<span class="cm"> */</span>
<span class="n">spinlock_t</span><span class="n">f_lock</span><span class="p">;</span>
<span class="k">enum</span> <span class="n">rw_hint</span><span class="n">f_write_hint</span><span class="p">;</span>
<span class="n">atomic_long_t</span><span class="n">f_count</span><span class="p">;</span>
<span class="kt">unsigned</span> <span class="kt">int</span> <span class="n">f_flags</span><span class="p">;</span>
<span class="n">fmode_t</span><span class="n">f_mode</span><span class="p">;</span>
<span class="k">struct</span> <span class="n">mutex</span><span class="n">f_pos_lock</span><span class="p">;</span>
<span class="n">loff_t</span><span class="n">f_pos</span><span class="p">;</span>
<span class="k">struct</span> <span class="n">fown_struct</span><span class="n">f_owner</span><span class="p">;</span>
<span class="k">const</span> <span class="k">struct</span> <span class="n">cred</span><span class="o">*</span><span class="n">f_cred</span><span class="p">;</span>
<span class="k">struct</span> <span class="n">file_ra_state</span><span class="n">f_ra</span><span class="p">;</span>

<span class="n">u64</span><span class="n">f_version</span><span class="p">;</span>
<span class="cp">#ifdef CONFIG_SECURITY</span>
<span class="kt">void</span><span class="o">*</span><span class="n">f_security</span><span class="p">;</span>
<span class="cp">#endif</span>
<span class="cm">/* needed for tty driver, and maybe others */</span>
<span class="kt">void</span><span class="o">*</span><span class="n">private_data</span><span class="p">;</span>

<span class="cp">#ifdef CONFIG_EPOLL</span>
<span class="cm">/* Used by fs/eventpoll.c to link all the hooks to this file */</span>
<span class="k">struct</span> <span class="n">hlist_head</span><span class="o">*</span><span class="n">f_ep</span><span class="p">;</span>
<span class="cp">#endif </span><span class="cm">/* #ifdef CONFIG_EPOLL */</span><span class="cp">
<span class="k">struct</span> <span class="n">address_space</span><span class="o">*</span><span class="n">f_mapping</span><span class="p">;</span>
<span class="n">errseq_t</span><span class="n">f_wb_err</span><span class="p">;</span>
<span class="n">errseq_t</span><span class="n">f_sb_err</span><span class="p">;</span> <span class="cm">/* for syncfs */</span>
<span class="p">&#125;</span> <span class="n">__randomize_layout</span>
  <span class="n">__attribute__</span><span class="p">((</span><span class="n">aligned</span><span class="p">(</span><span class="mi">4</span><span class="p">)));</span><span class="cm">/* lest something weird decides that 2 is OK */</span>
</span></span></code></pre></div><a href="http://link.zhihu.com/?target=https%3A//git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/include/linux/fs.h%3Fh%3Dv5.15%23n965" data-draft-node="block" data-draft-type="link-card" class=" external" target="_blank" rel="nofollow noreferrer"><span class="invisible">https://</span><span class="visible">git.kernel.org/pub/scm/</span><span class="invisible">linux/kernel/git/torvalds/linux.git/tree/include/linux/fs.h?h=v5.15#n965</span><span class="ellipsis"></span></a><p>虽然两边差异很大，但可以看到相似的成员有两个：</p><div class="highlight"><pre><code class="language-text"><span>FILE_OBJECT->FileName <===> file->f_path //文件路径
FILE_OBJECT->FsContext2 <===> file->private_data //驱动私有信息
</span></code></pre></div><p>而Linux还多了一个很关键的结构：file->f_inode</p><a href="http://link.zhihu.com/?target=https%3A//git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/include/linux/fs.h%3Fh%3Dv5.15%23n623" data-draft-node="block" data-draft-type="link-card" class=" external" target="_blank" rel="nofollow noreferrer"><span class="invisible">https://</span><span class="visible">git.kernel.org/pub/scm/</span><span class="invisible">linux/kernel/git/torvalds/linux.git/tree/include/linux/fs.h?h=v5.15#n623</span><span class="ellipsis"></span></a><p>inode结构对应的有点类似于Windows里的FCB，但FCB结构是各个文件系统自己定义的，比如FAT的定义：</p><a href="http://link.zhihu.com/?target=https%3A//github.com/microsoft/Windows-driver-samples/blob/master/filesys/fastfat/fatstruc.h%23L764" data-draft-node="block" data-draft-type="link-card" class=" external" target="_blank" rel="nofollow noreferrer"><span class="invisible">https://</span><span class="visible">github.com/microsoft/Wi</span><span class="invisible">ndows-driver-samples/blob/master/filesys/fastfat/fatstruc.h#L764</span><span class="ellipsis"></span></a><p>然后各自的文件系统驱动再通过<b>file --> inode</b>或者<b>FILE_OBJECT --> FCB</b>结构关联各自操作系统内核的cache管理部分，形成一套完整的cache管理机制（Windows通过FILE_OBJECT->SectionObjectPointer找到对应的cache内容）。</p><p>对比二者的区别的话，可以发现Linux在文件系统公共层（VFS）上有定义inode结构，而Windows没有，同时Linux的inode结构不是以名字索引的，而是以一个序号i_ino：</p><div class="highlight"><pre><code class="language-c"><span><span class="k">struct</span> <span class="n">inode</span> <span class="p">&#123;</span>
        <span class="cm">/*.....*/</span>
<span class="cm">/* Stat data, not accessed from path walking */</span>
<span class="kt">unsigned</span> <span class="kt">long</span><span class="n">i_ino</span><span class="p">;</span>
<span class="p">&#125;;</span>
</span></code></pre></div><p><b>问题就出在这里：</b></p><p><b>Windows的文件系统驱动里只能通过名字来索引FILE_OBJECT结构的，不像Linux那样可以通过序号（i_ino）来找到inode</b>，那么一旦一个文件的文件名处于无效的状态，那么内核就没办法检索出来一个文件名对应的FILE_OBJECT，以及它对应的cache节点。而一旦cache管理出了问题，那么内核是必然要崩溃的。</p><p>所以Windows不能这么做的原因是：</p><p>受限于FILE_OBJECT数据结构的设计（可能最早是因为FAT的设计问题），导致内核/文件系统驱动中不能正确处理重名FILE_OBJECT问题，<b>重名可能导致内核cache管理部分混乱，所以Windows不允许删除一个正在打开的文件</b>。这是一个内核设计的问题，上层的各种行为只是表面现象。</p><p>那么Windows的FILE_SHARE_DELETE是怎么回事呢？其实FILE_SHARE_DELETE并没有把文件真的删除。如果你创建了一个带FILE_SHARE_DELETE标记的文件，然后删除它，再创建一个重名的文件，Windows会提示你创建失败：</p><figure data-size="normal"><img src="https://pic4.zhimg.com/v2-8a8085344d537f34f20b8e58235a3e8b_1440w.jpg" data-caption data-size="normal" data-rawwidth="496" data-rawheight="279" data-default-watermark-src="https://pic4.zhimg.com/v2-52fa4b4dd6c13f9dbc70cbe6b188ae19_720w.jpg" class="origin_image zh-lightbox-thumb" data-original="https://pic4.zhimg.com/v2-8a8085344d537f34f20b8e58235a3e8b_r.jpg" referrerpolicy="no-referrer"></figure><p>所以，Windows仍然是以文件名的方式管理cache的。</p><p>因为Linux使用i_ino在这个序号来管理文件cache，不存在重名问题，所以自然可以删除文件不受影响。</p><p>顺便补充一下，各种杀毒软件的文件粉碎机，本质上就是干掉FILE_OBJECT->SectionObjectPointer里的数据结构，释放内核中对应的cache节点，这样FILE_OBJECT重名也不会波及到内核的cache管理导致蓝屏了。</p><hr><p>其实Windows是支持FILE_OPEN_BY_FILE_ID的动作的，但可能是因为兼容性的问题（<b>FILE_OBJECT改动会影响很多驱动</b>），所以微软只能保持现状，而Linux则不考虑兼容性问题，灵活性自然要好很多。</p><p>那么，这个算不算是Windows的设计失误？我个人认为<b>勉强算是，非要说bug是feature也是可以接受的</b>。Windows的这个行为导致了其文件系统与<b>POSIX规范不完全兼容</b>，对于一些开源软件来说，不算友好。当然了，微软为了兼容性做了很大的让步，甚至包括bug的兼容性，比如Win9x里内存free以后仍然可用的bug，跳过Windows9这个版本号等等，所以<b>为了文件系统的兼容性而保持这种行为也是可以理解的</b>。毕竟Windows是要考虑兼容性问题的，每个大版本的改动都会导致一些驱动不能正常工作，这对于用户来说是很难接受的。</p><p>Linux的fs.h变化很大，不过Linux里大部分软件都是开源的，所以只要重新编译一下就可以了，不过对于某些闭源软件来说，Linux这种频繁变动的设计也是很不友好的。</p><hr><p>补充：</p><p>其它回答和评论里提到，我这个只是描述不能删除的原因，<b>没有说为什么这么设计</b>。我个人感觉是已经说的很清楚了，就是兼容性的问题。展开来说就是：</p><p>Windows使用文件名作为内核对象(FILE_OBJECT)的唯一标识符 -> 文件名不能重名 -> 文件不能在打开状态下被删除。</p><p>如果继续向上追溯，是因为DOS时代的<b>文件系统FAT就没有inode的概念</b>，FAT的文件属性保存在目录里而不是单独的一个区域，<b>Win9x只支持FAT</b>。</p><p>inode的概念最早是从UNIX-like的文件系统中出现的，属于文件系统的另一个发展方向。Windows也试图在文件系统中引入类似inode的定义，比如NTFS的$MFT里就有类似inode的定义。</p><p>技术发展到今天，<b>文件系统的底层数据结构已经不是影响文件系统行为的决定性因素</b>，比如<b>FAT32没有inode，但在Linux上一样可以获得inode号</b>。所以到了今天，Windows不能删除一个打开的文件，本质上<b>不是技术能力问题</b>，也不是文件系统数据结构问题，<b>纯粹是为了保持兼容性而做出的牺牲</b>。</p><p></p>  
</div>
            