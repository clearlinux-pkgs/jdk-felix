Name     : jdk-felix
Version  : 1.0.2
Release  : 1
URL      : http://repo.maven.apache.org/maven2/org/apache/felix/felix/1.0.2/felix-1.0.2.pom
Source0  : http://repo.maven.apache.org/maven2/org/apache/felix/felix/1.0.2/felix-1.0.2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/maven-poms/felix.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/felix.xml \
%{buildroot}/usr/share/maven-poms/felix.pom \
%{buildroot}/usr/share/java/felix.jar \

%files
%defattr(-,root,root,-)
/usr/share/maven-metadata/felix.xml
/usr/share/maven-poms/felix.pom
