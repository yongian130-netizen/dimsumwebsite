const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('.nav');
toggle.addEventListener('click', () => {
  const isOpen = nav.classList.toggle('open');
  toggle.setAttribute('aria-expanded', String(isOpen));
});
nav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
  nav.classList.remove('open');
  toggle.setAttribute('aria-expanded', 'false');
}));
document.querySelector('#year').textContent = new Date().getFullYear();

document.querySelector('#share-site').addEventListener('click', async (event) => {
  event.preventDefault();
  if (location.protocol === 'file:') {
    alert(document.documentElement.lang === 'en' ? 'Publish the site to a public URL before sharing it on Facebook.' : '先把网站发布到公开网址，再分享给 Facebook 顾客。');
    return;
  }
  const shareUrl = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(location.href)}`;
  if (navigator.share) {
    try { await navigator.share({ title: document.title, text: document.documentElement.lang === 'en' ? 'Come by Longli Dim Sum House for handmade dim sum and tea.' : '来看看笼里点心茶楼，找个时间一起饮茶！', url: location.href }); }
    catch (error) { if (error.name !== 'AbortError') window.open(shareUrl, '_blank', 'noopener,noreferrer'); }
  } else {
    window.open(shareUrl, '_blank', 'noopener,noreferrer');
  }
});


