// 给 Windows exe 写入图标和名称。用法：node tools/patch-exe.js <输入exe> <输出exe>
const fs = require('fs'), R = require('resedit');
const [src, out] = process.argv.slice(2);
const exe = R.NtExecutable.from(fs.readFileSync(src));
const res = R.NtExecutableResource.from(exe);
const g = R.Resource.IconGroupEntry.fromEntries(res.entries);
const icon = R.Data.IconFile.from(fs.readFileSync(__dirname + '/../assets/icon.ico'));
R.Resource.IconGroupEntry.replaceIconsForResource(res.entries, g.length ? g[0].id : 101, g.length ? g[0].lang : 1033, icon.icons.map(i => i.data));
const vi = R.Resource.VersionInfo.fromEntries(res.entries)[0];
if (vi) {
  vi.setStringValues({ lang: 1033, codepage: 1200 }, { FileDescription: 'Inkling', ProductName: 'Inkling', InternalName: 'Inkling', OriginalFilename: 'Inkling.exe', CompanyName: 'Inkling', LegalCopyright: '' });
  vi.outputToResourceEntries(res.entries);
}
res.outputResource(exe);
fs.writeFileSync(out, Buffer.from(exe.generate()));
