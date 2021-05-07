
---
title: 'Linux系统安全强化指南'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=8067'
author: Dockone
comments: false
date: 2021-05-07 12:02:24
thumbnail: 'https://picsum.photos/400/300?random=8067'
---

<div>   
<br>本指南旨在说明如何尽可能地加强Linux的安全性和隐私性，并且不限于任何特定的指南。<br>
<br>免责声明：如果您不确定自己在做什么，请不要尝试在本文中使用任何内容。<br>
<br>本指南仅关注安全性和隐私性，而不关注性能，可用性或其他内容。列出的所有命令都将需要root特权。以“$”符号开头的单词表示一个变量，不同终端之间可能会有所不同。<br>
<h3>选择正确的Linux发行版</h3>选择一个好的Linux发行版有很多因素。<br>
<ul><li>避免分发冻结程序包，因为它们在安全更新中通常很落后。</li><li>不使用与Systemd机制的发行版。 Systemd包含许多不必要的攻击面；它尝试做的事情远远超出了必要，并且超出了初始化系统应做的事情。</li><li>使用musl作为默认的C库。 Musl专注于最小化，这会导致很小的攻击面，而其他C库（例如glibc）过于复杂，容易产生漏洞。例如，与musl中的极少数漏洞相比，glibc中的一百多个漏洞已被公开披露。尽管仅靠披露的CVE本身通常是不准确的统计信息，但有时这种情况有时可以用来表示过分的问题。 Musl还具有不错的漏洞利用缓解措施，尤其是其新的强化内存分配器。</li><li>最好默认情况下使用LibreSSL而不是OpenSSL的发行版。OpenSSL包含大量完全不必要的攻击面，并且遵循不良的安全做法。例如，它仍然保持OS / 2和VMS支持这些已有数十年历史的古老操作系统。这些令人讨厌的安全做法导致了可怕的Heartbleed漏洞。LibreSSL是OpenBSD团队的OpenSSL分支，它采用了出色的编程实践并消除了很多攻击面。在LibreSSL成立的第一年内，它缓解了许多漏洞，其中包括一些高严重性的漏洞。</li></ul><br>
<br>用作强化操作系统基础的最佳发行版是Gentoo Linux，因为它可以让您精确地配置系统，以达到理想的效果，这将非常有用，尤其是参考我们在后面的章节中使用更安全的编译标志。<br>
<br>但是，由于Gentoo的巨大可用性缺陷，它对于许多人来说可能并不顺手。在这种情况下，Void Linux的Musl构建是一个很好的折衷方案。<br>
<h3>内核</h3>内核是操作系统的核心，不幸的是很容易受到攻击。正如Brad Spengler曾经说过的那样，可以将其视为系统上最大，最易受攻击的setuid根二进制文件。因此，对内核进行尽可能多的强化非常重要。<br>
<h4>Stable vs LTS内核</h4>Linux内核以两种主要形式发布：稳定和长期支持（LTS）。稳定版本是较新的版本，而LTS发行版本是较老的稳定版本，长期以来一直受支持。选择上述任何一个发行版本都有许多后果。<br>
<br>Linux内核未使用CVE标识安全漏洞。这意味着大多数安全漏洞的修复程序不能向后移植到LTS内核。但是稳定版本包含到目前为止进行的所有安全修复。<br>
<br>但是，有了这些修复程序，稳定的内核将包含更多新功能，因此大大增加了内核的攻击面，并引入了大量新错误。相反，LTS内核的受攻击面较小，因为这些功能没有被不断添加。<br>
<br>此外，稳定的内核还包括更新的强化功能，以减轻LTS内核没有的某些利用。此类功能的一些示例是Lockdown LSM和STACKLEAK GCC插件。<br>
<br>总而言之，在选择稳定或LTS内核时需要权衡取舍。LTS内核具有较少的强化功能，并且并非当时所有的公共错误修复都已向后移植，但是通常它的攻击面更少，并且引入未知错误的可能性也较小。稳定的内核具有更多的强化功能，并且包括所有已知的错误修复，但它也具有更多的攻击面以及引入更多未知错误的机会更大。最后，最好使用较新的LTS分支（如4.19内核）。<br>
<h4>Sysctl</h4>Sysctl是允许用户配置某些内核设置并启用各种安全功能或禁用危险功能以减少攻击面的工具。要临时更改设置，您可以执行：<br>
<pre class="prettyprint">sysctl -w $tunable = $value<br>
</pre><br>
要永久更改sysctls，您可以将要更改的sysctls添加到/etc/sysctl.conf或/etc/sysctl.d中的相应文件，具体取决于您的Linux发行版。<br>
<br>以下是您应更改的建议sysctl设置。<br>
<br><strong>Kernel self-protection</strong><br>
<pre class="prettyprint">kernel.kptr_restrict=2<br>
</pre><br>
内核指针指向内核内存中的特定位置。这些在利用内核方面可能非常有用，但是默认情况下不会隐藏内核指针，例如，通过读取/proc/kallsyms的内容即可轻松发现它们。此设置旨在减轻内核指针泄漏。另外，您可以设置kernel.kptr_restrict = 1以仅从没有CAP_SYSLOG功能的进程中隐藏内核指针。<br>
<pre class="prettyprint">kernel.dmesg_restrict=1<br>
</pre><br>
dmesg是内核日志，它公开了大量有用的内核调试信息，但这通常会泄漏敏感信息，例如内核指针。更改上述sysctl设置会将内核日志限制为CAP_SYSLOG功能。<br>
<pre class="prettyprint">kernel.printk=3 3 3 3<br>
</pre><br>
尽管dmesg_restrict的值，启动过程中内核日志仍将显示在控制台中。能够在引导过程中记录屏幕的恶意软件可能会滥用此恶意软件以获得更高的特权。此选项可防止这些信息泄漏。必须将其与下面描述的某些引导参数结合使用才能完全有效。<br>
<pre class="prettyprint">kernel.unprivileged_bpf_disabled=1  <br>
net.core.bpf_jit_harden=2<br>
</pre><br>
eBPF暴露了很大的攻击面，因此需加以限制。这些系统将eBPF限制为CAP_BPF功能（在5.8之前的内核版本上为CAP_SYS_ADMIN），并启用JIT强化技术，例如常量绑定。<br>
<pre class="prettyprint">dev.tty.ldisc_autoload=0<br>
</pre><br>
这将加载TTY行规则限制为CAP_SYS_MODULE功能，以防止非特权的攻击者使用TIOCSETD ioctl加载易受攻击的线路规则，而该TIOCSETD ioctl之前已在许多漏洞利用中被滥用。<br>
<pre class="prettyprint">vm.unprivileged_userfaultfd=0<br>
</pre><br>
userfaultfd() 系统调用经常被滥用以利用“事后使用(use-after-free)”缺陷。因此，该sysctl用于将此syscall限制为CAP_SYS_PTRACE功能。<br>
<pre class="prettyprint">kernel.kexec_load_disabled=1<br>
</pre><br>
kexec是一个系统调用，用于在运行时引导另一个内核。可以滥用此功能来加载恶意内核并在内核模式下获得任意代码执行能力，因此该sysctl设置将被禁用。<br>
<pre class="prettyprint">kernel.sysrq=4<br>
</pre><br>
SysRq密钥向非特权用户公开了许多潜在的危险调试功能。与通常的假设相反，SysRq不仅是物理攻击的问题，而且还可以远程触发。该sysctl的值使其可以使用户只能使用SAK密钥，这对于安全地访问root是必不可少的。或者，您可以简单地将值设置为0以完全禁用SysRq。<br>
<pre class="prettyprint">kernel.unprivileged_userns_clone=0<br>
</pre><br>
用户名称空间是内核中的一项功能，旨在改善沙箱并使非特权用户易于访问它，但是，此功能公开了重要的内核攻击面，以进行特权升级，因此该sysctl将用户名称空间的使用限制为CAP_SYS_ADMIN功能。对于无特权的沙箱，建议使用具有很少攻击面的setuid二进制文件，以最大程度地减少特权升级的可能性。沙箱章节部分将进一步讨论此主题。<br>
<br>请注意，尽管该sysctl仅在某些Linux发行版中存在，因为它需要内核补丁。如果您的内核不包含此补丁，则可以通过设置user.max_user_namespaces = 0来完全禁用用户名称空间（包括root用户）。<br>
<pre class="prettyprint">kernel.perf_event_paranoid=3<br>
</pre><br>
性能事件会增加大量内核攻击面，并导致大量漏洞。此sysctl设置将性能事件的所有使用限制为CAP_PERFMON功能（5.8之前的内核版本为CAP_SYS_ADMIN）。<br>
<br>请注意，此sysctl设置需要在某些发行版中具备相关的内核补丁。否则，此设置等效于kernel.perf_event_paranoid = 2，它仅限制此功能的子集。<br>
<br><strong>网络</strong><br>
<pre class="prettyprint">net.ipv4.tcp_syncookies=1<br>
</pre><br>
这有助于防止SYN泛洪攻击，这种攻击是拒绝服务攻击的一种形式，在这种攻击中，攻击者发送大量虚假的SYN请求，以尝试消耗足够的资源以使系统对合法流量不响应。<br>
<pre class="prettyprint">net.ipv4.tcp_rfc1337=1<br>
</pre><br>
这通过丢弃处于时间等待状态的套接字的RST数据包来防止time-wait状态。<br>
<pre class="prettyprint">net.ipv4.conf.all.rp_filter=1  <br>
net.ipv4.conf.default.rp_filter=1<br>
</pre><br>
这些启用了源验证，以验证从计算机所有网络接口接收到的数据包。<br>
<pre class="prettyprint">net.ipv4.conf.all.accept_redirects=0  <br>
net.ipv4.conf.default.accept_redirects=0  <br>
net.ipv4.conf.all.secure_redirects=0  <br>
net.ipv4.conf.default.secure_redirects=0  <br>
net.ipv6.conf.all.accept_redirects=0  <br>
net.ipv6.conf.default.accept_redirects=0  <br>
net.ipv4.conf.all.send_redirects=0  <br>
net.ipv4.conf.default.send_redirects=0<br>
</pre><br>
这些设置禁用了ICMP重定向，以防止中间人攻击并最大程度地减少信息泄露。<br>
<pre class="prettyprint">net.ipv4.icmp_echo_ignore_all=1<br>
</pre><br>
此设置使您的系统忽略所有ICMP请求，以避免Smurf攻击，使设备更难以在网络上枚举，并防止通过ICMP时间戳识别时钟指纹。<br>
<pre class="prettyprint">net.ipv4.conf.all.accept_source_route=0  <br>
net.ipv4.conf.default.accept_source_route=0  <br>
net.ipv6.conf.all.accept_source_route=0  <br>
net.ipv6.conf.default.accept_source_route=0<br>
</pre><br>
源路由是一种允许用户重定向网络流量的机制。由于这可用于执行中间人攻击，在中间人攻击中，出于恶意目的将流量重定向，因此上述设置将会禁用此功能。<br>
<pre class="prettyprint">net.ipv6.conf.all.accept_ra=0  <br>
net.ipv6.conf.default.accept_ra=0<br>
</pre><br>
恶意的IPv6路由广告可能会导致中间人攻击，因此应将其禁用。<br>
<pre class="prettyprint">net.ipv4.tcp_sack=0  <br>
net.ipv4.tcp_dsack=0  <br>
net.ipv4.tcp_fack=0<br>
</pre><br>
禁用TCP SACK。ACK通常被利用，并且在许多情况下是不必要的，因此如果您不需要它，则应将其禁用。<br>
<br><strong>用户空间</strong><br>
<pre class="prettyprint">kernel.yama.ptrace_scope=2<br>
</pre><br>
ptrace是一个系统调用，它允许程序调试、修改和检查另一个正在运行的进程，从而使攻击者可以轻易修改其他正在运行的程序的内存。设置将ptrace的使用限制为仅具有CAP_SYS_PTRACE功能的进程。或者，将sysctl设置为3以完全禁用ptrace。<br>
<pre class="prettyprint">vm.mmap_rnd_bits=32  <br>
vm.mmap_rnd_compat_bits=16<br>
</pre><br>
ASLR是一种常见的漏洞利用缓解措施，它可以使进程的关键部分在内存中的位置随机化。这可能会使各种各样的漏洞利用更困难，因为它们首先需要信息泄漏。上述设置增加了用于mmap ASLR的熵的位数，从而提高了其有效性。<br>
<br>这些sysctls的值必须根据CPU体系结构进行设置。以上值与x86兼容，但其他体系结构可能有所不同。<br>
<pre class="prettyprint">fs.protected_symlinks=1  <br>
fs.protected_hardlinks=1<br>
</pre><br>
仅当在可全局写入的粘性目录之外，当符号链接和关注者的所有者匹配或目录所有者与符号链接的所有者匹配时，才允许遵循符号链接。这还可以防止没有对源文件的读/写访问权限的用户创建硬链接。这两者都阻止了许多常见的TOCTOU漏洞（time-of-check-to-time-of-use）。<br>
<pre class="prettyprint">fs.protected_fifos=2  <br>
fs.protected_regular=2<br>
</pre><br>
这些阻止了在可能由攻击者控制的环境（例如，全局可写目录）中创建文件，从而使数据欺骗攻击更加困难。<br>
<h4>引导参数</h4>引导参数在引导时使用引导加载程序（bootloader）将设置传递给内核。类似于sysctl，可以使用某些设置来提高安全性。引导加载程序通常在引导参数设置方式上有所不同。下面列出了一些示例，但是您应该研究特定bootloader的修改参数的必要步骤。<br>
<br>如果使用GRUB作为引导程序，请编辑/etc /default/grub并将参数添加到GRUB_CMDLINE_LINUX_DEFAULT=line。<br>
<br>如果使用Syslinux，请编辑/boot/syslinux/syslinux.cfg并将它们添加到APPEND行中。<br>
<br>如果使用systemd-boot，请编辑您的加载程序条目，并将其附加到linux行的末尾。<br>
<br>建议使用以下设置以提高安全性。<br>
<br><strong>Kernel self-protection</strong><br>
<pre class="prettyprint">slab_nomerge<br>
</pre><br>
这将禁用slab合并，这将通过防止覆盖合并的缓存中的对象并使其更难以影响slab缓存的布局，从而大大增加了堆利用的难度。<br>
<pre class="prettyprint">slub_debug=FZ<br>
</pre><br>
这些启用健全性检查（F）和重新分区（Z）。健全性检查会添加各种检查，以防止某些slab操作中的损坏。重新分区会在slab周围添加额外的区域，以检测slab何时被覆盖超过其实际大小，从而有助于检测溢出。<br>
<pre class="prettyprint">init_on_alloc=1 init_on_free=1<br>
</pre><br>
这样可以在分配和空闲时间期间将内存清零，这可以帮助减轻使用后使用的漏洞并清除内存中的敏感信息。如果您的内核版本低于5.3，则这些选项不存在。而是在上述slub_debug选项后面附加“ P”，以获得slub_debug=FZP并添加page_poison=1。由于它们实际上是一种调试功能，刚好具有一些安全性，因此它们在释放时提供的内存擦除形式较弱。<br>
<pre class="prettyprint">page_alloc.shuffle=1<br>
</pre><br>
此选项使页分配器空闲列表随机化，从而通过降低页分配的可预测性来提高安全性，同时这也提高了性能。<br>
<pre class="prettyprint">pti=on<br>
</pre><br>
这将启用内核页表隔离，从而减轻崩溃并防止某些KASLR绕过。<br>
<pre class="prettyprint">vsyscall=none<br>
</pre><br>
这将禁用vsyscall，因为它们已过时且已被vDSO取代。 vsyscall也在内存中的固定地址上，使其成为ROP攻击的潜在目标。<br>
<pre class="prettyprint">debugfs=off<br>
</pre><br>
这将禁用debugfs，它会公开许多有关内核的敏感信息。<br>
<pre class="prettyprint">oops=panic<br>
</pre><br>
有时某些内核漏洞利用会导致所谓的“oops”。此参数将引发内核对此类事件panic，从而防止这些攻击。但是，有时错误的驱动程序会导致无害的操作，这会导致系统崩溃，这意味着此引导参数只能在某些硬件上使用。<br>
<pre class="prettyprint">module.sig_enforce=1<br>
</pre><br>
这仅允许加载已使用有效密钥签名的内核模块，使加载恶意内核模块更加困难。<br>
<br>这可以防止加载所有树外内核模块（包括DKMS模块），除非您已对其进行签名，这意味着诸如VirtualBox或Nvidia驱动程序之类的模块可能不可用，但根据您的设置可能并不重要。<br>
<pre class="prettyprint">lockdown=confidentiality<br>
</pre><br>
内核锁定LSM可以消除用户空间代码滥用以升级为内核特权并提取敏感信息的许多方法。为了在用户空间和内核之间实现清晰的安全边界，此LSM是必需的。上面的选项在confidentiality模式（最严格的选项）中启用此功能。这意味着module.sig_enforce=1。<br>
<pre class="prettyprint">mce=0<br>
</pre><br>
这将导致内核对ECC内存中无法利用的错误panic，而这些错误可能会被利用。对于没有ECC内存的系统，这是不必要的。<br>
<pre class="prettyprint">quiet loglevel=0<br>
</pre><br>
这些参数可防止引导期间信息泄漏，并且必须与上面的kernel.printk sysctl结合使用。<br>
<br><strong>CPU缓解</strong><br>
<br>最好启用适用于您的CPU的所有CPU缓解措施，以确保您不受已知漏洞的影响。这是启用所有内置缓解措施的列表：<br>
<pre class="prettyprint">spectre_v2=on spec_store_bypass_disable=on tsx=off tsx_async_abort=full,nosmt mds=full,nosmt l1tf=full,force nosmt=force kvm.nx_huge_pages=force<br>
</pre><br>
您必须研究系统受其影响的CPU漏洞，并相应地选择上述缓解措施。请记住，您将需要安装微代码更新，以完全免受这些漏洞的影响。但所有这些操作都可能导致性能显着下降。<br>
<br><strong>结果</strong><br>
<br>如果遵循了以上所有建议（不包括特定的CPU缓解措施），则将具有：<br>
<pre class="prettyprint">slab_nomerge slub_debug=FZ init_on_alloc=1 init_on_free=1 page_alloc.shuffle=1 pti=on vsyscall=none debugfs=off oops=panic module.sig_enforce=1 lockdown=confidentiality mce=0 quiet loglevel=0<br>
</pre><br>
如果将GRUB用作引导加载程序，则可能需要重新生成GRUB配置文件才能应用这些文件。<br>
<h4>hidepid</h4>/proc是一个伪文件系统，其中包含有关系统上当前正在运行的所有进程的信息。默认情况下，所有用户都可以访问此程序，这可能使攻击者可以窥探其他进程。要只允许用户看到自己的进程，而不能看到其他用户的进程，则必须使用hidepid=2，gid=proc挂载选项来挂载/proc。gid=proc将proc组从此功能中排除，因此您可以将特定的用户或进程列入白名单。添加这些选项的一种方法是编辑/etc/fstab并添加：<br>
<pre class="prettyprint">proc /proc proc nosuid,nodev,noexec,hidepid=2,gid=proc 0 0<br>
</pre><br>
systemd-logind仍然需要查看其他用户的进程，因此，要使用户会话在systemd系统上正常工作，必须创建/etc/systemd/system/systemd-logind.service.d/hidepid.conf并添加：<br>
<pre class="prettyprint">[Service]  <br>
SupplementaryGroups=proc<br>
</pre><br>
<h4>减少内核攻击面</h4>最好禁用不是绝对必要的任何功能，以最大程度地减少潜在的内核攻击面。这些功能不必一定很危险，它们可以只是被删除以减少攻击面的良性代码。切勿禁用您不了解的随机事物。以下是一些可能有用的示例，具体取决于您的设置。<br>
<br><strong>引导参数</strong><br>
<br>引导参数通常可以用来减少攻击面，这样的例子之一是：<br>
<pre class="prettyprint">ipv6.disable=1<br>
</pre><br>
这将禁用整个IPv6堆栈，如果您尚未迁移到该堆栈，则可能不需要该堆栈。如果正在使用的IPv6，请不要使用此引导参数。<br>
<br><strong>将内核模块列入黑名单</strong><br>
<br>内核允许非特权的用户通过模块自动加载来间接导致某些模块被加载。这使攻击者可以自动加载易受攻击的模块，然后加以利用。一个这样的示例是CVE-2017-6074，其中攻击者可以通过启动DCCP连接来触发DCCP内核模块的加载，然后利用该内核模块中的漏洞。<br>
<br>可以通过将文件插入/etc/modprobe.d并将指定的内核模块列入黑名单的方法，将特定的内核模块列入黑名单。<br>
<br>Install参数告诉modprobe运行特定命令，而不是像往常一样加载模块。 /bin/false是仅返回1的命令，该命令实际上不会执行任何操作。两者都告诉内核运行/bin/false 而不是加载模块，这将防止攻击者利用该模块。以下是最有可能不需要的内核模块：<br>
<pre class="prettyprint">install dccp /bin/false  <br>
install sctp /bin/false  <br>
install rds /bin/false  <br>
install tipc /bin/false  <br>
install n-hdlc /bin/false  <br>
install ax25 /bin/false  <br>
install netrom /bin/false  <br>
install x25 /bin/false  <br>
install rose /bin/false  <br>
install decnet /bin/false  <br>
install econet /bin/false  <br>
install af_802154 /bin/false  <br>
install ipx /bin/false  <br>
install appletalk /bin/false  <br>
install psnap /bin/false  <br>
install p8023 /bin/false  <br>
install p8022 /bin/false  <br>
install can /bin/false  <br>
install atm /bin/false<br>
</pre><br>
特别是模糊的网络协议会增加大量的远程攻击面。此黑名单：<br>
<ul><li>DCCP — Datagram Congestion Control Protocol</li><li>SCTP — Stream Control Transmission Protocol</li><li>RDS — Reliable Datagram Sockets</li><li>TIPC — Transparent Inter-process Communication</li><li>HDLC — High-Level Data Link Control</li><li>AX25 — Amateur X.25</li><li>NetRom</li><li>X25</li><li>ROSE</li><li>DECnet</li><li>Econet</li><li>af_802154 — IEEE 802.15.4</li><li>IPX — Internetwork Packet Exchange</li><li>AppleTalk</li><li>PSNAP — Subnetwork Access Protocol</li><li>p8023 — Novell raw IEEE 802.3</li><li>p8022 — IEEE 802.2</li><li>CAN — Controller Area Network</li><li>ATM</li></ul><br>
<br><pre class="prettyprint">install cramfs /bin/false  <br>
install freevxfs /bin/false  <br>
install jffs2 /bin/false  <br>
install hfs /bin/false  <br>
install hfsplus /bin/false  <br>
install squashfs /bin/false  <br>
install udf /bin/false<br>
</pre><br>
将各种稀有文件系统列入黑名单。<br>
<pre class="prettyprint">install cifs /bin/true  <br>
install nfs /bin/true  <br>
install nfsv3 /bin/true  <br>
install nfsv4 /bin/true  <br>
install gfs2 /bin/true<br>
</pre><br>
如果不使用网络文件系统，也可以将其列入黑名单。<br>
<pre class="prettyprint">install vivid /bin/false<br>
</pre><br>
vivid driver[1]驱动程序仅用于测试目的，并且是特权提升漏洞的原因，因此应禁用它。<br>
<pre class="prettyprint">install bluetooth /bin/false  <br>
install btusb /bin/false<br>
</pre><br>
禁用具有安全问题历史记录的蓝牙。<br>
<pre class="prettyprint">install uvcvideo /bin/false<br>
</pre><br>
这会禁用网络摄像头，以防止其被用来监视您。<br>
<br>您也可以将麦克风模块列入黑名单，但这在系统之间可能会有所不同。要查找模块的名称，请在/proc/asound/modules中查找并将其列入黑名单。例如，一个这样的模块是snd_hda_intel。<br>
<br>请注意，尽管有时麦克风的内核模块与扬声器的模块相同。这意味着像这样禁用麦克风也可能会无意中禁用任何扬声器，虽然扬声器也有可能变成麦克风，所以这不一定是消极的结果。<br>
<br>最好从物理上删除这些设备，或者至少在BIOS/UEFI中禁用它们。禁用内核模块并不总是那么有效。<br>
<br><strong>rfkill</strong><br>
<br>可以通过rfkill将无线设备列入黑名单，以进一步减少远程攻击面。要将所有无线设备列入黑名单，请执行：<br>
<pre class="prettyprint">rfkill block all<br>
</pre><br>
WiFi可以通过以下方式解锁：<br>
<pre class="prettyprint">rfkill unblock wifi<br>
</pre><br>
在使用systemd的系统上，rfkill在所有会话中均保持不变，但是，在使用其他init系统的系统上，您可能必须创建一个init脚本以在引导时执行这些命令。<br>
<h4>其他内核指针泄漏</h4>前面的部分已经防止了一些内核指针泄漏，但是还有更多泄漏。<br>
<br>在文件系统上，/boot中存在内核映像和System.map文件。/usr/src和/&#123;,usr/&#125; lib/modules目录中还有其他敏感的内核信息。您应该限制这些目录的文件权限，以使它们只能由root用户读取。您还应该删除System.map文件，因为除高级调试外，它们都不需要。<br>
<br>此外，某些日志记录守护程序（例如systemd的journalctl）包括内核日志，可用于绕过上述dmesg_restrict保护。从adm组中删除用户通常足以撤销对以下日志的访问：<br>
<pre class="prettyprint">gpasswd -d $user adm<br>
</pre><br>
<h4>限制对sysfs的访问</h4>sysfs是伪文件系统，可提供大量的内核和硬件信息。它通常安装在/sys上。 sysfs导致大量信息泄漏，尤其是内核指针泄漏。Whonix的security-misc软件包包括hide-hardware-info脚本，该脚本限制访问此目录以及/proc中的一些脚本，以试图隐藏潜在的硬件标识符并防止内核指针泄漏。该脚本是可配置的，并允许基于组将特定的应用程序列入白名单。建议应用此方法，并使其在启动时使用init脚本执行。或者<a href="https://github.com/Whonix/security-misc/blob/master/lib/systemd/system/hide-hardware-info.service">这样做成systemd服务</a>。<br>
<br>为了使基本功能在使用systemd的系统上运行，必须将一些系统服务列入白名单。这可以通过创建/etc/systemd/system/user@.service.d/sysfs.conf并添加以下内容来完成：<br>
<pre class="prettyprint">[Service]  <br>
SupplementaryGroups=sysfs<br>
</pre><br>
但是，这不能解决所有问题。许多应用程序可能仍会中断，您需要将它们正确列入白名单。<br>
<h4>Linux强化</h4>某些发行版（例如Arch Linux）包括强化的内核程序包。它包含许多强化补丁程序和更注重安全性的内核配置。如果可能的话，建议安装它。<br>
<h4>Grsecurity</h4>Grsecurity是一组内核修补程序，可以大大提高内核安全性。这些补丁曾经可以免费获得，但是现在需要购买了。如果可用，则强烈建议您获取它。Grsecurity提供了最新的内核和用户空间保护。<br>
<h4>内核运行时防护</h4>Linux Kernel Runtime Guard（LKRG）是一个内核模块，可确保运行时内核的完整性并检测漏洞。它可以杀死整个类别的内核漏洞。但这并不是一个完美的缓解方法，因为LKRG在设计上可以绕开。它仅适用于现成的恶意软件。但是，尽管可能性不大，但LKRG本身可能会像其他任何内核模块一样公开新的漏洞。<br>
<h4>自编译内核</h4>建议编译您自己的内核，同时启用尽可能少的内核模块和尽可能多的安全性功能，以将内核的受攻击面保持在绝对最低限度。<br>
<br>另外，应用内核强化补丁，例如如上所述的linux-hardened或grsecurity。<br>
<br>发行版编译的内核还具有公共内核指针/符号，这对于漏洞利用非常有用。编译自己的内核将为您提供独特的内核符号，连同kptr_restrict，dmesg_restrict和其他针对内核指针泄漏的强化措施，将使攻击者更加难以创建依赖于内核指针知识的漏洞利用程序。<br>
<br>您就可以从Whonix的强化内核中汲取灵感或使用它。<br>
<h3>强制访问措施</h3>强制访问控制（MAC）系统对程序可以访问的内容进行细粒度的控制。这意味着您的浏览器将无权访问您的整个主目录或类似目录。<br>
<br>最常用的MAC措施是SELinux和AppArmor。SELinux比AppArmor更安全，因为它的粒度更细。例如，它是基于inode而不是基于路径的，允许强制执行明显更严格的限制，可以过滤内核ioctl等。不幸的是，这是以难以使用和难以学习为代价的，因此某些人可能会首选AppArmor。<br>
<br>要在内核中启用AppArmor，必须设置以下引导参数：<br>
<pre class="prettyprint">apparmor=1 security=apparmor<br>
</pre><br>
要启用SELinux，请设置以下参数：<br>
<pre class="prettyprint">selinux=1 security=selinux<br>
</pre><br>
请记住，仅启用MAC措施本身并不能神奇地提高安全性。您必须制定严格的政策才能充分利用它。例如，要创建AppArmor配置文件，请执行：<br>
<pre class="prettyprint">aa-genprof $path_to_program<br>
</pre><br>
打开程序，然后像往常一样开始使用它。AppArmor将检测需要访问哪些文件，并将它们添加到配置文件中（如果您选择的话）。但是，仅凭这一点不足以提供高质量的配置文件。请参阅AppArmor文档[5]以获取更多详细信息。<br>
<br>如果您想更进一步，则可以通过实施initramfs勾子来设置一个完整的系统MAC策略，该策略限制每个单个用户空间进程，该挂钩对init系统强制实施MAC策略。这就是Android使用SELinux的方式，以及Whonix未来将如何使用AppArmor的方式。对于加强实施最小特权原则的强大安全模型是必要的。<br>
<h3>沙箱</h3><h4>应用沙箱</h4>沙箱可让您在隔离的环境中运行程序，该环境对系统的其余部分具有有限的访问权限或完全没有访问权限。您可以使用它们来保护应用程序安全或运行不受信任的程序。<br>
<br>建议与AppArmor或SELinux一起在单独的用户帐户中使用Bubblewrap[6]到沙箱程序。您也可以考虑改用gVisor，它的优点是为每个来宾提供了自己的内核。<br>
<br>这些方法中的任何一个都可以用来创建一个功能强大的沙箱，并且暴露的攻击面最小。如果您不想自己创建沙箱，请在完成后考虑使用Whonix的sandbox-app-launcher。您不应该使用Firejail。<br>
<br>诸如Docker和LXC之类的容器解决方案经常被误导为沙盒形式。它们太宽松了，无法广泛支持各种应用程序，因此不能认为它们是强大的应用程序沙箱。<br>
<h4>常见沙箱逃逸</h4><strong>PulseAudio</strong><br>
<br>PulseAudio是一种常见的声音服务器，但在编写时并未考虑隔离或沙盒的问题，这使其成为重复出现的沙盒逃逸漏洞。为了防止这种情况，建议您从沙箱中阻止对PulseAudio的访问，或者从系统中完全卸载它。<br>
<br><strong>D-Bus</strong><br>
<br>D-Bus是台式机Linux上最流行的进程间通信形式，但它也是沙箱逃逸的另一种常见途径，因为它允许与服务自由交互。这些漏洞的一个例子就是Firejail。您应该从沙箱中阻止对D-Bus的访问，或者通过MAC以细粒度的规则进行调解。<br>
<br><strong>GUI隔离</strong><br>
<br>任何Xorg窗口都可以访问另一个窗口。这允许琐碎的键盘记录或屏幕截图程序，甚至可以记录诸如root密码之类的内容。您可以使用嵌套的X11服务器（例如Xpra或Xephyr和bubblewrap）将Xorg窗口沙箱化。默认情况下，Wayland将窗口彼此隔离，这将是一个比Xorg更好的选择，尽管Wayland可能不如Xorg普遍可用，因为它在开发中较早。<br>
<br><strong>ptrace</strong><br>
<br>如前所述，ptrace是一个系统调用，可能会被滥用破坏在沙箱外部运行的进程。为避免这种情况，您可以通过sysctl启用内核YAMA ptrace限制，也可以在seccomp过滤器中将ptrace syscall列入黑名单。<br>
<br><strong>TIOCSTI</strong><br>
<br>TIOCSTI是一个ioctl，它允许注入终端命令，并为攻击者提供了一种简单的机制，可以在同一用户会话内的其他进程之间横向移动。可以通过将seccomp过滤器中的ioctl列入黑名单或使用bubblewrap的--new-session参数来缓解这种攻击。<br>
<h4>Systemd沙箱</h4>虽然不建议使用systemd，但有些系统可能无法切换。这些人至少可以使用沙盒服务，因此他们只能访问所需的内容。这是一个沙箱化systemd服务的示例：<br>
<pre class="prettyprint">[Service]  <br>
CapabilityBoundingSet=CAP_NET_BIND_SERVICE  <br>
ProtectSystem=strict  <br>
ProtectHome=true  <br>
ProtectKernelTunables=true  <br>
ProtectKernelModules=true  <br>
ProtectControlGroups=true  <br>
ProtectKernelLogs=true  <br>
ProtectHostname=true  <br>
ProtectClock=true  <br>
ProtectProc=invisible  <br>
ProcSubset=pid  <br>
PrivateTmp=true  <br>
PrivateUsers=yes  <br>
PrivateDevices=true  <br>
MemoryDenyWriteExecute=true  <br>
NoNewPrivileges=true  <br>
LockPersonality=true  <br>
RestrictRealtime=true  <br>
RestrictSUIDSGID=true  <br>
RestrictAddressFamilies=AF_INET  <br>
RestrictNamespaces=yes  <br>
SystemCallFilter=write read openat close brk fstat lseek mmap mprotect munmap rt_sigaction rt_sigprocmask ioctl nanosleep select access execve getuid arch_prctl set_tid_address set_robust_list prlimit64 pread64 getrandom  <br>
SystemCallArchitectures=native  <br>
UMask=0077  <br>
IPAddressDeny=any  <br>
AppArmorProfile=/etc/apparmor.d/usr.bin.example<br>
</pre><br>
所有选项的说明：<br>
<ul><li><code class="prettyprint">CapabilityBoundingSet=</code>— Specifies the  capabilities[8]the process is given.</li><li><code class="prettyprint">ProtectHome=true</code>— Makes all home directories inaccessible.</li><li><code class="prettyprint">ProtectKernelTunables=true</code>— Mounts kernel tunables such as those modified through<code class="prettyprint">sysctl</code>as read-only.</li><li><code class="prettyprint">ProtectKernelModules=true</code>— Denies module loading and unloading.</li><li><code class="prettyprint">ProtectControlGroups=true</code>— Mounts all control group hierarchies as read-only.</li><li><code class="prettyprint">ProtectKernelLogs=true</code>— Prevents accessing the kernel logs.</li><li><code class="prettyprint">ProtectHostname=true</code>— Prevents changes to the system hostname.</li><li><code class="prettyprint">ProtectClock</code>— Prevents changes to the system clock.</li><li><code class="prettyprint">ProtectProc=invisible</code>— Hides all outside processes.</li><li><code class="prettyprint">ProcSubset=pid</code>— Permits access to only the pid subset of<code class="prettyprint">/proc</code>.</li><li><code class="prettyprint">PrivateTmp=true</code>— Mounts an empty tmpfs over<code class="prettyprint">/tmp</code>and<code class="prettyprint">/var/tmp</code>, therefore hiding their previous contents.</li><li><code class="prettyprint">PrivateUsers=true</code>— Sets up an empty user namespace to hide other user accounts on the system.</li><li><code class="prettyprint">PrivateDevices=true</code>— Creates a new<code class="prettyprint">/dev</code>mount with minimal devices present.</li><li><code class="prettyprint">MemoryDenyWriteExecute=true</code>— Enforces a memory W^X policy.</li><li><code class="prettyprint">NoNewPrivileges=true</code>— Prevents escalating privileges.</li><li><code class="prettyprint">LockPersonality=true</code>— Locks down the<code class="prettyprint">personality()</code>syscall to prevent switching execution domains.</li><li><code class="prettyprint">RestrictRealtime=true</code>— Prevents attempts to enable realtime scheduling.</li><li><code class="prettyprint">RestrictSUIDSGID=true</code>— Prevents executing setuid or setgid binaries.</li><li><code class="prettyprint">RestrictAddressFamilies=AF_INET</code>— Restricts the usable socket address families to IPv4 only (<code class="prettyprint">AF_INET</code>).</li><li><code class="prettyprint">RestrictNamespaces=true</code>— Prevents creating any new namespaces.</li><li><code class="prettyprint">SystemCallFilter=...</code>— Restricts the allowed syscalls to the absolute minimum. If you aren't willing to maintain your own custom seccomp filter, then systemd provides many <a href="https://www.freedesktop.org/software/systemd/man/systemd.exec.html#System%20Call%20Filtering">predefined system call sets</a> that you can use.<code class="prettyprint">@system-service</code>will be suitable for many use cases.</li><li><code class="prettyprint">SystemCallArchitectures=native</code>— Prevents executing syscalls from other CPU architectures.</li><li><code class="prettyprint">UMask=0077</code>— Sets the  umask[9]to a more restrictive value.</li><li><code class="prettyprint">IPAddressDeny=any</code>— Blocks all incoming and outgoing traffic to/from any IP address. Set<code class="prettyprint">IPAddressAllow=</code>to configure a whitelist. Alternatively, setup a network namespace with<code class="prettyprint">PrivateNetwork=true</code>.</li><li><code class="prettyprint">AppArmorProfile=...</code>— Runs the process under the specified AppArmor profile.</li></ul><br>
<br>您不能仅将此示例配置复制到您的配置中，每种服务的要求各不相同，并且必须针对每种服务微调沙箱。要了解有关您可以设置的所有选项的更多信息，请阅读<a href="https://www.freedesktop.org/software/systemd/man/systemd.exec.html">systemd.exec手册页</a>。<br>
<br>如果您使用的系统不是systemd而是init，那么可以使用bubblewrap轻松复制所有这些选项。<br>
<h4>gVisor</h4>普通沙箱固有地与主机共享同一内核。您信任我们已经评估为不安全的内核，可以正确限制这些程序。由于主机内核的整个攻击面已完全暴露，因此沙盒中的内核利用程序可以绕过任何限制。已经进行了一些努力来限制使用seccomp的攻击面，但不足以完全解决此问题。<br>
<br>GVisor是解决此问题的方法。它为每个应用程序提供了自己的内核，该内核以内存安全的语言重新实现了Linux内核的大部分系统调用，从而提供了明显更强的隔离性。<br>
<h4>虚拟机</h4>虽然不是传统的“沙盒”，但虚拟机通过虚拟化全新系统来分离进程，从而提供了非常强大的隔离性。KVM是内核模块，它允许内核充当管理程序，而QEMU是利用KVM的仿真器。Virt-manager和GNOME Boxs都是良好且易于使用的GUI，用于管理KVM / QEMU虚拟机。不建议使用Virtualbox的原因有很多。<br>
<h3>强化内存分配器</h3>hardened_malloc是一种硬化的内存分配器，可为堆内存损坏漏洞提供实质性的保护。它很大程度上基于OpenBSD的malloc设计，但具有许多改进。<br>
<br>可以通过LD_PRELOAD环境变量针对每个应用程序使用hardened_malloc。例如，假设您编译的库位于/usr/lib/libhardened_malloc.so，则可以执行：<br>
<pre class="prettyprint">LD_PRELOAD="/usr/lib/libhardened_malloc.so" $program<br>
</pre><br>
通过全局预加载该库，也可以在系统范围内使用它，这是使用它的推荐方法。为此，请编辑/etc/ld.so.preload并插入：<br>
<pre class="prettyprint">/usr/lib/libhardened_malloc.so<br>
</pre><br>
尽管大多数应用程序都可以正常工作，但hardened_malloc可能会破坏某些应用程序。建议使用以下选项编译hardened_malloc以最大程度地减少损坏：<br>
<pre class="prettyprint">CONFIG_SLAB_QUARANTINE_RANDOM_LENGTH=0 CONFIG_SLAB_QUARANTINE_QUEUE_LENGTH=0 CONFIG_GUARD_SLABS_INTERVAL=8<br>
</pre><br>
您还应该使用sysctl设置以下内容，以适应hardened_malloc创建的大量保护页：<br>
<pre class="prettyprint">vm.max_map_count=524240<br>
</pre><br>
Whonix项目为基于Debian的发行版提供了hardened_malloc软件包。<br>
<h3>强化编译标志</h3>编译自己的程序可以带来很多好处，因为它使您能够优化程序的安全性。但是，执行完全相反的操作并降低安全性很容易，如果您不确定自己在做什么，请跳过本节。在基于源的发行版（例如Gentoo）上，这将是最简单的，但也可以在其他发行版上这样做。<br>
<br>某些编译选项可用于添加其他漏洞利用缓解措施，从而消除整个类别的常见漏洞。您可能听说过常规保护，例如位置独立可执行文件，堆栈粉碎保护程序，立即绑定，只读重定位和FORTIFY_SOURCE，但是本节将不做介绍，因为它们已被广泛采用。相反，它将讨论诸如控制流完整性和影子堆栈之类的现代漏洞利用缓解措施。<br>
<br>本节涉及主要用C或C ++编写的本机程序。您必须使用Clang编译器，因为这些功能在GCC上不可用。请记住，由于未广泛采用这些缓解措施，因此某些应用程序在启用它们后可能无法运行。<br>
<br>控制流完整性（CFI）是一种缓解漏洞利用的方法，旨在防止诸如ROP或JOP之类的代码重用攻击。由于更广泛采用的缓解措施（例如NX）使过时的利用技术过时了，因此使用这些技术利用了很大一部分漏洞。Clang支持细粒度的前沿CFI，这意味着它可以有效缓解JOP攻击。Clang的CFI本身并不能减轻ROP；您还必须使用下面记录的单独机制。要启用此功能，必须应用以下编译标志： <br>
<pre class="prettyprint">-flto -fvisibility=hidden -fsanitize=cfi<br>
</pre><br>
影子堆栈通过将程序复制到其他隐藏堆栈中来保护程序的返回地址。然后比较主堆栈和影子堆栈中的返回地址，看两者是否不同。如果是这样，则表明存在攻击，程序将中止，从而减轻了ROP攻击。Clang具有称为ShadowCallStack的功能，可以完成此操作，但是，仅在ARM64上可用。要启用此功能，必须应用以下编译标志：<br>
<pre class="prettyprint">-fsanitize=shadow-call-stack<br>
</pre><br>
如果上述ShadowCallStack不是一个选项，则可以选择使用具有相似目标的SafeStack。但是，不幸的是，此功能有许多漏洞，因此效果不甚理想。如果仍然希望启用此功能，则必须应用以下编译标志：<br>
<pre class="prettyprint">-fsanitize=safe-stack<br>
</pre><br>
最常见的内存损坏漏洞之一是未初始化的内存。Clang有一个选项可以使用零或特定模式自动初始化变量。建议将变量初始化为零，因为使用其他模式比利用漏洞缓解功能更适合发现错误。要启用此功能，必须应用以下编译标志：<br>
<pre class="prettyprint">-ftrivial-auto-var-init=zero -enable-trivial-auto-var-init-zero-knowing-it-will-be-removed-from-clang<br>
</pre><br>
但该选项的存在目前正在<a href="https://lists.llvm.org/pipermail/cfe-dev/2020-April/065221.html">辩论</a>中。<br>
<h3>内存安全语言</h3>用内存安全语言编写的程序会自动受到保护，免受各种安全漏洞的影响，这些安全漏洞包括缓冲区溢出，未初始化的变量，售后使用等。Microsoft和Google的安全研究人员进行的研究证明，已发现的大多数漏洞都是内存安全问题。这样的内存安全语言的示例包括Rust，Swift和Java，而内存不安全语言的示例包括C和C ++。如果可行，应使用内存安全替代品替换尽可能多的程序。<br>
<h3>Root账户</h3>root可以执行任何操作，并且可以访问您的整个系统。因此，应尽可能将其锁定，以使攻击者无法轻松获得root用户访问权限。<br>
<h4>/etc/securetty</h4>/etc/securetty文件指定允许您以root用户身份登录的位置。该文件应保留为空，以便任何人都不能从终端上这样做。<br>
<h4>限制su</h4>su可让您从终端切换用户。默认情况下，它尝试以root用户身份登录。要将su的使用限制在wheel组中，请编辑/etc/pam.d/su和/etc/pam.d/su-l并添加：<br>
<pre class="prettyprint">auth required pam_wheel.so use_uid<br>
</pre><br>
您应该在wheel组中拥有尽可能少的用户。<br>
<h4>锁定root账户</h4>要锁定root帐户以防止任何人以root身份登录，请执行：<br>
<pre class="prettyprint">passwd -l root<br>
</pre><br>
在执行此操作之前，请确保您具有获取根的替代方法（例如，从活动USB引导并更改为文件系统的chroot），以免您无意中将自己锁定在系统之外。<br>
<h4>拒绝通过SSH的远程root登陆</h4>为了防止某人通过SSH以root身份登录，请编辑/etc/ssh/sshd_config并添加：<br>
<pre class="prettyprint">PermitRootLogin no<br>
</pre><br>
<h4>增加散列回合数</h4>您可以增加shadow使用的哈希回合数，从而通过迫使攻击者计算更多的哈希值来破解您的密码，从而提高哈希密码的安全性。默认情况下，shadow使用5000次回合，但是您可以将其增加到任意数量。尽管配置的回合越多，登录速度就越慢。编辑/etc/pam.d/passwd并添加回合选项。<br>
<pre class="prettyprint">password required pam_unix.so sha512 shadow nullok rounds=65536<br>
</pre><br>
这使shadow执行65536次散列回合。<br>
<br>应用此设置后，密码不会自动重新加密，因此您需要使用以下方法重置密码：<br>
<pre class="prettyprint">passwd $username<br>
</pre><br>
<h4>限制Xorg root访问</h4>默认情况下，某些发行版以root用户身份运行Xorg，这是一个问题，因为Xorg包含大量古老而又复杂的代码，这增加了巨大的攻击面，并使其更有可能拥有可以获取root特权的漏洞利用程序。要阻止它作为root用户执行，请编辑/etc/X11/Xwrapper.config并添加：<br>
<pre class="prettyprint">needs_root_rights = no<br>
</pre><br>
<h4>安全访问root</h4>恶意软件可以使用多种方法来嗅探root帐户的密码。因此，访问根帐户的传统方式是不安全的，最好根本不访问根，但这实际上是不可行的。本节详细介绍了访问根帐户的最安全方法。在安装操作系统后，应立即应用这些说明，以确保该软件不含恶意软件。<br>
<br>您绝对不能使用普通用户帐户访问root，因为root可能已被盗用。您也不能直接登录到根帐户。通过执行以下操作，创建一个单独的“管理员”用户帐户，该帐户仅用于访问root用户，而不能用于访问其他用户：<br>
<pre class="prettyprint">useradd admin<br>
</pre><br>
执行并来设置一个非常强的密码：<br>
<pre class="prettyprint">passwd admin<br>
</pre><br>
仅允许该帐户使用您首选的权限提升机制。例如，如果使用sudo，则通过执行以下命令来添加sudoers异常：<br>
<pre class="prettyprint">visudo -f /etc/sudoers.d/admin-account<br>
</pre><br>
然后输入：<br>
<pre class="prettyprint">admin ALL=(ALL) ALL<br>
</pre><br>
确保没有其他帐户可以访问sudo（或您的首选机制）<br>
<br>现在，要实际登录到该帐户，请先重新启动-例如，这可以防止受损的窗口管理器执行登录欺骗。当提供登录提示时，请通过按键盘上的以下组合键来激活安全注意键：<br>
<pre class="prettyprint">Alt + SysRq + k<br>
</pre><br>
这将杀死当前虚拟控制台上的所有应用程序，从而克服登录欺骗攻击。现在，您可以安全地登录到您的管理员帐户，并使用root用户执行任务。完成后，注销管理员帐户，然后重新登录到非特权用户帐户。<br>
<h3>防火墙</h3>防火墙可以控制传入和传出的网络流量，并且可以用来阻止或允许某些类型的流量。除非有特殊原因，否则应始终阻止所有传入流量。建议设置严格的iptables或nftables防火墙。火墙必须针对您的系统进行微调，并且没有一个适合所有防火墙的规则集。建议您熟悉创建防火墙规则。Arch Wiki[14]和手册页[15]都是很好的资源。<br>
<br>这是基本iptables配置的示例，该配置禁止所有传入的网络流量：<br>
<pre class="prettyprint">*filter  <br>
:INPUT DROP [0:0]  <br>
:FORWARD DROP [0:0]  <br>
:OUTPUT ACCEPT [0:0]  <br>
:TCP - [0:0]  <br>
:UDP - [0:0]  <br>
-A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT  <br>
-A INPUT -i lo -j ACCEPT  <br>
-A INPUT -m conntrack --ctstate INVALID -j DROP  <br>
-A INPUT -p udp -m conntrack --ctstate NEW -j UDP  <br>
-A INPUT -p tcp --tcp-flags FIN,SYN,RST,ACK SYN -m conntrack --ctstate NEW -j TCP  <br>
-A INPUT -p udp -j REJECT --reject-with icmp-port-unreachable  <br>
-A INPUT -p tcp -j REJECT --reject-with tcp-reset  <br>
-A INPUT -j REJECT --reject-with icmp-proto-unreachable  <br>
COMMIT<br>
</pre><br>
但是，您不应尝试在实际系统上使用此示例。它仅适用于某些台式机系统。<br>
<h3>身份标识</h3>为了保护隐私，最好最大程度地减少可追溯到您的信息量。<br>
<h4>主机名和用户名</h4>请勿在主机名或用户名中添加唯一标识的内容。将它们保留为通用名称，例如“host”和“user”，以便它们无法识别您。<br>
<h4>Timezones / Locales / Keymaps</h4>如果可能，应将您的时区设置为“ UTC”，将区域设置和键盘映射设置为“ US”。<br>
<h4>机器ID</h4>一个独一无二的机器ID被存储在/var/lib/dbus/machine-id （systemd系统是保存在/etc/machine-id）这些应编辑为通用名称，例如Whonix ID：<br>
<pre class="prettyprint">b08dfa6083e7567a1921a715000001fb<br>
</pre><br>
<h4>MAC地址欺骗</h4>MAC地址是分配给网络接口控制器（NIC）的唯一标识符。每次您连接到网络时（WIFI或以太网）则您的MAC地址已暴露。这使人们可以使用它来跟踪您并在本地网络上唯一地标识您。<br>
<br>但您不应该完全随机化MAC地址。拥有完全随机的MAC地址是显而易见的，并且会对您脱颖而出的行为产生不利影响。<br>
<br>MAC地址的OUI（组织唯一标识符）部分标识芯片组的制造商。对MAC地址的这一部分进行随机化处理可能会为您提供以前从未使用过的OUI，数十年来从未使用过的OUI或在您所在的地区极为罕见的OUI，因此使您脱颖而出，很明显地表明您在欺骗MAC地址。<br>
<br>MAC地址的末尾标识您的特定设备，并且可以用来跟踪您的设备。仅对MAC地址的这一部分进行随机化可防止您被跟踪，同时仍使MAC地址看起来可信。<br>
<br>要欺骗这些地址，请首先执行以下命令找出您的网络接口名称：<br>
<pre class="prettyprint">ip a<br>
</pre><br>
接下来，安装macchanger并执行：<br>
<pre class="prettyprint">macchanger -e $network_interface<br>
</pre><br>
要在每次引导时随机分配MAC地址，您应该为您的特定初始化系统创建一个初始化脚本。这是systemd的一个示例：<br>
<pre class="prettyprint">[Unit]  <br>
Description=macchanger on eth0  <br>
Wants=network-pre.target  <br>
Before=network-pre.target  <br>
BindsTo=sys-subsystem-net-devices-eth0.device  <br>
After=sys-subsystem-net-devices-eth0.device  <br>
<br>
[Service]  <br>
ExecStart=/usr/bin/macchanger -e eth0  <br>
Type=oneshot  <br>
<br>
[Install]  <br>
WantedBy=multi-user.target<br>
</pre><br>
上面的示例在启动时欺骗了eth0接口的MAC地址。将eth0替换为您的网络接口。<br>
<h4>时间攻击</h4>几乎每个系统都有不同的时间。这可用于时钟偏斜指纹攻击，几毫秒的差异足以使用户被暴露识别。<br>
<br><strong>ICMP时间戳</strong><br>
<br>ICMP时间戳会在查询答复中泄漏系统时间。阻止这些攻击的最简单方法是利用防火墙阻止传入连接，或者使内核忽略ICMP请求。<br>
<br><strong>TCP时间戳</strong><br>
<br>TCP时间戳也会泄漏系统时间。内核尝试通过对每个连接使用随机偏移量来解决此问题，但这不足以解决问题。因此应该禁用TCP时间戳，可以通过使用sysctl设置以下内容来完成：<br>
<pre class="prettyprint">net.ipv4.tcp_timestamps=0<br>
</pre><br>
<strong>TCP初始化序号</strong><br>
<br>TCP初始序列号（ISN）是泄漏系统时间的另一种方法。为了减轻这种情况，您必须安装tirdad内核模块，该模块会生成用于连接的随机ISN。<br>
<br><strong>时间同步</strong><br>
<br>时间同步对于匿名性和安全性至关重要。错误的系统时钟可能使您遭受时钟偏斜指纹攻击，或者可以用来为您提供过时的HTTPS证书，从而绕过证书到期或吊销。<br>
<br>最流行的时间同步方法NTP是不安全的，因为它未经加密和未经身份验证，因此攻击者可以轻易地拦截和修改请求。NTP还会以NTP时间戳格式泄漏本地系统时间，该格式可用于时钟偏斜指纹识别，如前所述。<br>
<br>因此，您应该卸载所有NTP客户端并禁用systemd-timesyncd（如果正在使用）。您可以通过安全连接（HTTPS或最好是Torion服务）连接到受信任的网站，而不是NTP，并从HTTP标头中提取当前时间。达到此目的的工具是sdwdate或我自己的安全时间同步工具。<br>
<h4>按键指纹</h4>可以通过他们在键盘上输入键的方式来对人进行指纹识别。您可以通过键入速度，在两次按键之间的暂停，每次按键被按下和释放的确切时间等方式来唯一地进行指纹识别。可以使用KeyTrac在线进行测试。<br>
<br>Kloak是一种工具，旨在通过混淆按键和释放事件之间的时间间隔来克服这种跟踪方法。当按键被按下时，它会引入随机延迟，然后由应用程序选择。<br>
<h3>文件权限</h3>默认情况下，文件的权限是非常宽松的。您应该在整个系统中搜索权限不当的文件和目录，并对其进行限制。例如，在诸如Debian之类的某些发行版中，用户的Home目录是全局可读的。<br>
<br>这可以通过执行以下操作来限制：<br>
<pre class="prettyprint">chmod 700 /home/$user<br>
</pre><br>
另外一些示例是/boot，/usr /src和/ &#123;,usr /&#125; lib/modules 它们包含内核映像，System.map和其他各种文件，所有这些文件都可能泄漏有关内核的敏感信息。<br>
<pre class="prettyprint">chmod 700 /boot /usr/src /lib/modules /usr/lib/modules<br>
</pre><br>
在基于Debian的发行版中，必须使用dpkg-statoverride保留文件许可权。否则，它们将在更新期间被覆盖。<br>
<br>Whonix的SUID Disabler和Permission Hardener[22]会自动应用本节中详细介绍的步骤。<br>
<h4>setuid / setgid</h4>Setuid / SUID允许用户使用二进制文件所有者的特权执行二进制文件。这通常用于允许非特权用户使用通常仅为root用户保留的某些功能。因此，许多SUID二进制文件都有特权升级安全漏洞的历史记录。 Setgid / SGID类似，但适用于组而不是用户。要使用setuid或setgid位查找系统上的所有二进制文件，请执行：<br>
<pre class="prettyprint">find / -type f \( -perm -4000 -o -perm -2000 \)<br>
</pre><br>
然后，您应该删除不使用的程序上的所有不必要的setuid / setgid位，或将其替换为功能。要删除setuid位，请执行：<br>
<pre class="prettyprint">chmod u-s $path_to_program<br>
</pre><br>
要删除setgid位，执行：<br>
<pre class="prettyprint">chmod g-s $path_to_program<br>
</pre><br>
要向文件添加功能，请执行：<br>
<pre class="prettyprint">setcap $capability+ep $path_to_program<br>
</pre><br>
或者，要删除不必要的功能，请执行：<br>
<pre class="prettyprint">setcap -r $path_to_program<br>
</pre><br>
<h4>umask</h4>umask设置新创建文件的默认文件权限。默认的umask是0022，它不是很安全，因为它为系统上的每个用户提供了对新创建文件的读取访问权限。要使所有者以外的任何人都不可读新文件，请编辑/etc/profile并添加：<br>
<pre class="prettyprint">umask 0077<br>
</pre><br>
<h3>核心转储</h3>核心转储包含特定时间（通常是该程序崩溃时）该程序的已记录内存。它们可能包含敏感信息，例如密码和加密密钥，因此必须将其禁用。<br>
<br>禁用它们的方法主要有三种：sysctl，systemd和ulimit<br>
<h4>sysctl</h4>通过sysctl设置以下设置：<br>
<pre class="prettyprint">kernel.core_pattern=|/bin/false<br>
</pre><br>
<h4>systemd</h4>创建/etc/systemd/coredump.conf.d/disable.conf并添加如下内容：<br>
<pre class="prettyprint">[Coredump]  <br>
Storage=none<br>
</pre><br>
<h4>ulimit</h4>编辑/etc/security/limits.conf并添加如下内容：<br>
<pre class="prettyprint">* hard core 0<br>
</pre><br>
<h4>setuid进程</h4>即使在进行了这些设置之后，以提升的特权运行的进程仍可能会转储其内存。<br>
<br>为了防止他们这样做，请通过sysctl设置以下内容：<br>
<pre class="prettyprint">fs.suid_dumpable=0<br>
</pre><br>
<h3>Swap</h3>与核心转储类似，交换或分页将部分内存复制到磁盘，其中可能包含敏感信息。应该将内核配置为仅在绝对必要时进行交换，相应的sysctl设置：<br>
<pre class="prettyprint">vm.swappiness=1<br>
</pre><br>
<h3>PAM</h3>PAM是用于用户身份验证的框架。这就是您登录时使用的机制。您可以通过要求使用强密码或在失败的登录尝试后强制执行延迟验证来使其更加安全。<br>
<br>要强制使用强密码，可以使用pam_pwquality。它强制执行密码的可配置策略。例如，如果您希望密码至少包含16个字符（最小），与旧密码（difok）至少6个不同的字符，至少3个数字（dcredit），至少2个大写字母（ucredit），至少2个字符小写字母（lcredit）和至少3个其他字符（ocredit），然后编辑/etc/pam.d/passwd并添加：<br>
<pre class="prettyprint">password required pam_pwquality.so retry=2 minlen=16 difok=6 dcredit=-3 ucredit=-2 lcredit=-2 ocredit=-3 enforce_for_root  <br>
password required pam_unix.so use_authtok sha512 shadow<br>
</pre><br>
要强制执行延迟验证，可以使用pam_faildelay。要在两次失败的登录尝试之间添加至少4秒的延迟以阻止暴力破解尝试，请编辑/etc/pam.d/system-login并添加：<br>
<pre class="prettyprint">auth optional pam_faildelay.so delay=4000000<br>
</pre><br>
4000000 是4秒（以微秒为单位）。<br>
<h3>Microcode更新</h3>Microcode更新对于修复关键的CPU漏洞（如Meltdown和Spectre等）至关重要。大多数发行版都将这些发行版包含在其软件仓库中，例如Arch Linux和Debian。<br>
<h3>IPv6隐私扩展</h3>IPv6地址是从计算机的MAC地址生成的，从而使您的IPv6地址是唯一的，并直接绑定到计算机。隐私扩展会生成一个随机的IPv6地址，以减轻这种形式的跟踪。请注意，如果您开启了MAC地址欺骗机制或禁用了IPv6，则无需执行这些步骤。<br>
<br>要启用这些功能，请通过sysctl设置以下设置：<br>
<pre class="prettyprint">net.ipv6.conf.all.use_tempaddr=2  <br>
net.ipv6.conf.default.use_tempaddr=2<br>
</pre><br>
<h4>NetworkManager</h4>要为NetworkManager启用隐私扩展，请编辑/etc/NetworkManager/NetworkManager.conf并添加：<br>
<pre class="prettyprint">[connection]  <br>
ipv6.ip6-privacy=2<br>
</pre><br>
<h4>systemd-networkd</h4>要为systemd-networkd启用隐私扩展，请创建/etc/systemd/network/ipv6-privacy.conf并添加：<br>
<pre class="prettyprint">[Network]  <br>
IPv6PrivacyExtensions=kernel<br>
</pre><br>
<h3>分区和挂载选项</h3>文件系统应分为多个分区，以对其权限进行细粒度控制。可以添加不同的安装选项以限制可以执行的操作：<br>
<ul><li>nodev - 禁止使用设备</li><li>nosuid - 禁止setuid或setgid位</li><li>noexec - 禁止执行任何二进制文件</li></ul><br>
<br>这些安装选项应在/etc/fstab中尽可能设置。如果您不能使用单独的分区，请创建绑定挂载。一个更安全的/etc/fstab的示例：<br>
<pre class="prettyprint">/        /          ext4    defaults                              1 1  <br>
/home    /home      ext4    defaults,nosuid,noexec,nodev          1 2  <br>
/tmp     /tmp       ext4    defaults,bind,nosuid,noexec,nodev     1 2  <br>
/var     /var       ext4    defaults,bind,nosuid                  1 2  <br>
/boot    /boot      ext4    defaults,nosuid,noexec,nodev          1 2<br>
</pre><br>
请注意，可以通过shell脚本绕过noexec。<br>
<h3>熵</h3>熵基本上反应操作系统信息收集的随机程度，对于诸如加密之类的事情至关重要。因此，最好通过安装其他随机数生成器（如haveged和jitterentropy）从各种来源收集尽可能多的熵。<br>
<br>为了使jitterentropy正确运行，必须通过创建/usr/lib/modules-load.d/jitterentropy.conf并添加以下内容尽早加载内核模块：<br>
<pre class="prettyprint">jitterentropy_rng<br>
</pre><br>
<h4>RDRAND</h4>RDRAN是提供随机数的CPU指令。如果可用，内核会自动将其用作熵源。但是由于它是专有的并且是CPU本身的一部分，因此无法审核和验证其安全性。您甚至无法对代码进行反向工程。该RNG以前曾遭受过漏洞的攻击，其中有些可能是后门攻击。通过设置以下引导参数可以不信任此功能：<br>
<pre class="prettyprint">random.trust_cpu=off<br>
</pre><br>
<h3>以root身份编辑文件</h3>建议不要以root用户身份运行普通的文本编辑器。大多数文本编辑器可以做的不仅仅是简单地编辑文本文件，而且还可以被利用。例如，以root身份打开vi并输入：sh。现在，您具有一个可以访问整个系统的root shell，攻击者可以轻松利用该shell。<br>
<br>解决方案是使用sudoedit。这会将文件复制到一个临时位置，以普通用户身份打开文本编辑器，编辑该临时文件并以root用户身份覆盖原始文件。这样，实际的编辑器就不会以root身份运行。要使用sudoedit，执行：<br>
<pre class="prettyprint">sudoedit $path_to_file<br>
</pre><br>
默认情况下，它使用vi，但是可以通过EDITOR或SUDO_EDITOR环境变量来切换默认编辑器。例如，要使用nano，请执行：<br>
<pre class="prettyprint">EDITOR=nano sudoedit $path_to_file<br>
</pre><br>
可以在/etc/environment中全局设置此环境变量。<br>
<h3>特定发行版的安全强化</h3><h4>HTTP包管理器镜像</h4>默认情况下，Linux发行版通常使用HTTP或HTTP和HTTPS镜像的混合来从其软件存储库下载软件包。人们认为这很好，因为程序包管理器会在安装前验证程序包的签名。但是，从历史上看，已经有很多绕过此方法的地方。您应将软件包管理器配置为从HTTPS镜像专门下载以进行深度防御。<br>
<h4>APT seccomp-bpf</h4>自软件包管理器Debian Buster以来，APT已支持可选的seccomp-bpf过滤。这限制了允许执行APT的系统调用，这可能严重限制攻击者尝试利用APT中的漏洞时对系统造成危害的能力。要启用此功能，请创建/etc/apt/apt.conf.d/40sandbox并添加：<br>
<pre class="prettyprint">APT::Sandbox::Seccomp "true";<br>
</pre><br>
<h3>物理安全</h3>全盘加密可确保对驱动器上的所有数据进行加密，并且不会被物理攻击者读取。大多数发行版都支持在安装过程中启用加密，请确保设置了强密码。您也可以使用dm-crypt[28]手动加密驱动器。<br>
<br>请注意，全盘加密不包括/boot，这样仍然可以修改内核、引导加载程序和其他关键文件。为了完全防止篡改，您还必须实施经过验证的引导。<br>
<h4>BIOS / UEFI强化</h4>如果您仍在使用旧版BIOS，则应迁移到UEFI，以利用较新的安全功能。大多数BIOS或UEFI实现都支持设置密码。最好启用它并设置一个非常强壮的密码。虽然这是很弱的保护，因为重置密码很简单。它通常存储在易失性内存中，因此攻击者只需要能够卸下CMOS电池几秒钟，或者他们就可以使用某些主板上的跳线将其重置。<br>
<br>您还应该禁用所有未使用的设备和引导选项，例如USB引导，以减少攻击面。<br>
<br>别忽略BIOS或UEFI的更新，确保将其更新。将其与常规操作系统更新一样重要。<br>
<br>此外，请参阅《<a href="https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance">NSA的硬件和固件安全指南</a>》。<br>
<h4>Bootloader密码</h4>引导加载程序会在引导过程的早期执行，并负责加载操作系统。保护它非常重要，否则，它可能会被篡改。例如，本地攻击者可以通过在启动时使用init=/bin/bash作为内核参数来轻松获得root shell，该命令告诉内核执行/bin/bash而不是常规的init系统。您可以通过为引导加载程序设置密码来防止这种情况。仅设置引导程序密码不足以完全保护它。还必须按照以下说明设置经过验证的启动。<br>
<br><strong>Grub</strong><br>
<br>要为GRUB设置密码，请执行：<br>
<pre class="prettyprint">grub-mkpasswd-pbkdf2<br>
</pre><br>
输入您的密码，该密码将生成一个字符串。它将类似于“ grub.pbkdf2.sha512.10000.C4009... ”。创建/etc/grub.d/40_password并添加：<br>
<pre class="prettyprint">set superusers="$username"  <br>
password_pbkdf2 $username $password<br>
</pre><br>
用grub-mkpasswd-pbkdf2生成的字符串替换“$username”将用于被允许使用GRUB命令行，编辑菜单项和执行任何菜单项的超级用户。对于大多数人来说，这只是“root”。<br>
<br>重新生成您的配置文件，GRUB现在将受到密码保护。<br>
<br>要仅限制编辑引导参数并访问GRUB控制台，同时仍然允许您引导，请编辑 /boot/grub/grub.cfg并在 “menuentry '$OSName' ”旁边添加“ --unrestricted”参数。<br>
<pre class="prettyprint">menuentry 'Arch Linux' --unrestricted<br>
</pre><br>
您将需要再次重新生成配置文件以应用此更改。<br>
<br><strong>Syslinux</strong><br>
<br>Syslinux可以设置主密码或菜单密码。引导任何条目都需要主密码，而引导特定条目仅需要菜单密码。<br>
<br>要为Syslinux设置主密码，请编辑/boot/syslinux/syslinux.cfg并添加：<br>
<pre class="prettyprint">MENU MASTER PASSWD $password<br>
</pre><br>
要设置菜单密码，请编辑/boot/syslinux/syslinux.cfg，并在带有您要密码保护的项目的标签内，添加：<br>
<pre class="prettyprint">MENU PASSWD $password<br>
</pre><br>
将“ $password”替换为您要设置的密码。<br>
<br>这些密码可以是纯文本，也可以使用MD5，SHA-1，SHA-256或SHA-512进行散列。建议先使用强哈希算法（例如SHA-256或SHA-512）对密码进行哈希处理，以避免将其存储为明文形式。<br>
<br><strong>systemd-boot</strong><br>
<br>systemd-boot具有防止在引导时编辑内核参数的选项。在loader.conf文件中，添加：<br>
<pre class="prettyprint">editor no<br>
</pre><br>
systemd-boot并不正式支持保护内核参数编辑器的密码，但是您可以使用systemd-boot-password来实现[30]。<br>
<h4>验证引导</h4>经过验证的引导通过密码验证来确保引导链和基本系统的完整性。这可用于确保物理攻击者无法修改设备上的软件。<br>
<br>如果没有经过验证的引导，则一旦获得物理访问权限，就可以轻松绕过上述所有预防措施。经过验证的引导不仅像许多人认为的那样是为了物理安全。它还可以用于防止远程恶意软件持久化——如果攻击者设法破坏了整个系统并获得了很高的特权，则经过验证的引导将在重新引导后还原其更改，并确保它们无法持久化。<br>
<br>经过验证的最常见的引导实现是UEFI安全引导，但是它本身并不是一个完整的实现，因为它仅会验证引导加载程序和内核，这意味着可以通过以下方法：<br>
<ul><li>仅UEFI安全启动就没有一成不变的信任根，因此物理攻击者仍然可以刷新设备的固件。为了减轻这种情况，请结合使用UEFI安全启动和Intel Boot Guard或AMD Secure Boot。</li><li>远程攻击者（或不使用加密的物理攻击者）可以简单地修改操作系统的任何其他特权部分。例如，如果他们有修改内核的特权，那么他们也可以修改/sbin/init来有效地获得相同的结果。因此，仅验证内核和引导加载程序不会对远程攻击者产生任何影响。为了减轻这种情况，您必须使用dm-verity[31]验证基本操作系统，尽管由于传统Linux发行版的布局，这非常困难且笨拙。</li></ul><br>
<br>通常，很难在传统Linux上实现可靠的经过验证的引导实现。<br>
<h4>USBs</h4>USB设备为物理攻击提供了重要的攻击面。例如BadUSB和Stuxnet是此类攻击的范例。最佳实践是禁止所有新连接的USB且仅将受信任设备列入白名单，USBGuard对此非常有用。<br>
<br>您也可以将nousb用作内核引导参数，以禁用内核中的所有USB支持。可以sysctl设置kernel.deny_new_usb=1<br>
<h4>DMA攻击</h4>直接内存访问（DMA）攻击涉及通过插入某些物理设备来完全访问所有系统内存。这可以通过控制设备可访问的内存区域的IOMMU或将特别易受攻击的内核模块列入黑名单来缓解。<br>
<br>要启用IOMMU，请设置以下内核引导参数：<br>
<pre class="prettyprint">intel_iommu=on amd_iommu=on<br>
</pre><br>
您只需要为特定的CPU制造商启用该选项，但同时启用这两个选项就没有问题。<br>
<pre class="prettyprint">efi=disable_early_pci_dma<br>
</pre><br>
通过在非常早的启动过程中禁用所有PCI桥接器上的busmaster位，此选项可修复上述IOMMU中的漏洞。<br>
<br>此外，Thunderbolt和FireWire通常容易受到DMA攻击。要禁用它们，请将这些内核模块列入黑名单：<br>
<pre class="prettyprint">install firewire-core /bin/false  <br>
install thunderbolt /bin/false<br>
</pre><br>
<h4>冷启动攻击</h4>当攻击者在擦除RAM中的数据之前对其进行分析时，就会发生冷启动攻击。使用现代RAM时，冷启动攻击不太实用，因为RAM通常会在几秒钟或几分钟内清除，除非将其放入冷却液（如液氮或冷冻机）中。攻击者必须在几秒钟内将设备中的RAM棒拔出并将其暴露于液氮中，而且确保用户不会注意到。<br>
<br>如果冷启动攻击是威胁模型的一部分，请在关机后保护计算机几分钟，以确保没有人可以访问您的RAM记忆棒。您也可以将RAM棒焊接到主板上，以使其更难以卡住。如果使用笔记本电脑，请取出电池，然后直接用充电电缆供电。关机后请拔出电缆，以确保RAM彻底断电无法访问。<br>
<br>在内核自我保护启动参数部分中，空闲时内存清零选项将用零覆盖内存中的敏感数据。此外，强化的内存分配器可以通过CONFIG_ZERO_ON_FREE配置选项清除用户空间堆内存中的敏感数据。尽管如此，某些数据仍可能保留在内存中。<br>
<br>此外，现代内核还包括复位攻击缓解措施，该命令可命令固件在关机时擦除数据，尽管这需要固件支持。<br>
<br>确保正常关闭计算机，以使上述缓解措施可以开始。<br>
<br>如果以上都不适用您的威胁模型，则可以实施Tails的内存擦除过程，该过程将擦除大部分内存（视频内存除外），并且已被证明是有效的。<br>
<h3>最佳实践</h3>一旦对系统进行了尽可能多的加固，就应该遵循良好的隐私和安全性惯例：<br>
<ul><li>禁用或删除不需要的东西以最小化攻击面。</li><li>保持更新。配置cron任务或init脚本以每天更新系统。</li><li>不要泄漏有关您或您的系统的任何信息，无论它看起来多么渺小。</li><li>遵循常规的安全和隐私建议</li></ul><br>
<br>尽管已经进行了强化，但您必须记住Linux仍然是一个有缺陷的操作系统，没有任何强化可以完全修复它。<br>
<h3>其他指南</h3>您应该进行尽可能多的研究，而不要依赖单一的信息来源。最大的安全问题之一就是用户。这些是我认为有价值的其他指南的链接：<br>
<br>Arch Linux Security wiki page：<a href="https://wiki.archlinux.org/index.php/Security" rel="nofollow" target="_blank">https://wiki.archlinux.org/index.php/Security</a><br>
<br>Whonix Documentation：<a href="https://www.whonix.org/wiki/Documentation" rel="nofollow" target="_blank">https://www.whonix.org/wiki/Documentation</a><br>
<br>NSA RHEL 5 Hardening Guide(稍有过时，但仍包含有用的信息）：<a href="https://apps.nsa.gov/iaarchive/library/ia-guidance/security-configuration/operating-systems/guide-to-the-secure-configuration-of-red-hat-enterprise.cfm" rel="nofollow" target="_blank">https://apps.nsa.gov/iaarchive ... e.cfm</a><br>
<br>KSPP recommended kernel settings：<a href="https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings" rel="nofollow" target="_blank">https://kernsec.org/wiki/index ... tings</a><br>
<br>kconfig-hardened-check：<a href="https://github.com/a13xp0p0v/kconfig-hardened-check/" rel="nofollow" target="_blank">https://github.com/a13xp0p0v/k ... heck/</a><br>
<h3>术语</h3>您可能需要重新生成GRUB配置，以应用对引导加载程序所做的某些更改。在不同的发行版之间，执行此操作的步骤有时可能会有所不同。例如，在诸如Arch Linux之类的发行版上，应通过执行以下命令来重新生成配置文件：<br>
<pre class="prettyprint">grub-mkconfig -o $path_to_grub_config<br>
</pre><br>
"$path_to_grub_config" 取决于您如何设置系统。它通常是/boot/grub/grub.cfg或/boot/EFI/grub/grub.cfg，但是在执行此命令之前，请务必确保正确。<br>
<br>另外，在Debian或Ubuntu等发行版上，您应该执行以下命令：<br>
<pre class="prettyprint">update-grub<br>
</pre><br>
<h3>能力</h3>在Linux内核中，“ root特权”分为各种不同的能力（capabilities）。这在应用最小特权原则时很有帮助——可以给它们仅授予特定的子集，而不是授予进程总的root特权。例如，如果程序只需要设置系统时间，则只需要CAP_SYS_TIME而不是root所有能力。这会限制可能造成的损害，但是，您仍必须谨慎授予能力，因为无论如何，其中许多能力可能会被滥用以获取完整的root特权。<br>
<br>译文链接：<a href="https://blog.gaochao.me/post/645734976535543808/linux" rel="nofollow" target="_blank">https://blog.gaochao.me/post/6 ... linux</a>系统安全强化指南
                                
                                                              
</div>
            